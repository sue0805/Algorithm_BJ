import requests
import json
from collections import defaultdict

uri = 'http://localhost:8000'


def start(problem, elevators):
    return requests.post(uri + '/start/SUE/' + str(problem) + '/' + str(elevators)).json()


def call(token):
    header = {'X-Auth-Token': token}
    return requests.get(uri + '/oncalls', headers=header).json()


def action(token, commands):
    header = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    commands = json.dumps(commands)
    return requests.post(uri + '/action', headers=header, data=commands).json()


def simulate():
    token, time, elevators, is_end = start(2, 4).values()
    MAXPASS, MAXFLOOR, TOTALCALL = 8, 25, 500
    is_end = False
    elv_dir = ["DOWN"] * 4
    first = True

    while not is_end:
        t, ts, elevators, calls, is_end = call(token).values()
        check = defaultdict(bool)
        commands = {'commands' : [{} for i in range(4)]}
        for id in range(4):
            commands['commands'][id]['call_ids'] = list()
        empty_elvs = []
        for ev in elevators:
            id, floor, passengers, status = ev.values()
            commands['commands'][id]['elevator_id'] = id
            if (id == 0) and first:
                if floor < MAXFLOOR:
                    commands['commands'][id]['command'] = "UP"
                    continue
                if floor == MAXFLOOR:
                    first = False
            if status == 'UPWARD' or status == 'DOWNWARD': # 운행중?
                print('운행중')
                if passengers: # 승객 있나?
                    for p in passengers:
                        i, ts, st, end = p.values()
                        if end == floor: # 내릴 승객?
                            commands['commands'][id]['command'] = 'STOP'
                            break
                if 'command' not in commands['commands'][id]: # 승객이 없거나 내릴 승객이 없습니까?
                    if len(passengers) < MAXPASS:
                        for c in calls:
                            i, ts, st, end = c.values()
                            if st == floor: # 탈 승객?
                                if status == 'UPWARD' and end > floor:
                                    commands['commands'][id]['command'] = 'STOP'
                                    break
                                elif status == "DOWNWARD" and end < floor:
                                    commands['commands'][id]['command'] = 'STOP'
                                    break
                    if 'command' not in commands['commands'][id]: # 탈 승객도 없고, 내릴 승객도 없다
                        if floor == MAXFLOOR or floor == 1:
                            commands['commands'][id]['command'] = 'STOP'
                        else:
                            if passengers:
                                commands['commands'][id]['command'] = elv_dir[id]
                            else:
                                commands['commands'][id]['command'] = 'STOP'
            else: # 운행중 아님
                print('운행중 아님')
                if status == 'OPENED': # 열려있습니까?
                    print('열려있음')
                    if passengers:
                        for p in passengers:
                            i, ts, st, end = p.values()
                            if end == floor: # 내릴 승객
                                commands['commands'][id]['command'] = 'EXIT'
                                commands['commands'][id]['call_ids'].append(i)
                    if not commands['commands'][id]['call_ids']: # 내릴 승객 없다
                        print('내릴 승객 없다')
                        tmp = []
                        for c in calls:
                            i, ts, st, end = c.values()
                            if st == floor and len(commands['commands'][id]['call_ids']) + len(passengers) < MAXPASS:
                                # if elv_dir[id] == 'UP' and end > floor:
                                #     commands['commands'][id]['command'] = 'ENTER'
                                #     commands['commands'][id]['call_ids'].append(i)
                                #     tmp.append(c)
                                # elif elv_dir[id] == 'DOWN' and end < floor:
                                #     commands['commands'][id]['command'] = 'ENTER'
                                #     commands['commands'][id]['call_ids'].append(i)
                                #     tmp.append(c)
                                if passengers:
                                    i_, ts_, st_, end_ = passengers[0].values()
                                    if (end_ > floor and end > floor) or (end_ < floor and end < floor):
                                        commands['commands'][id]['command'] = 'ENTER'
                                        commands['commands'][id]['call_ids'].append(i)
                                        tmp.append(c)
                                else:
                                    commands['commands'][id]['command'] = 'ENTER'
                                    commands['commands'][id]['call_ids'].append(i)
                                    tmp.append(c)
                        if tmp: # 탈 승객
                            print('탈 승객 있다')
                            while tmp:
                                calls.remove(tmp.pop())
                        else: # 탈 승객 없다
                            commands['commands'][id]['command'] = "CLOSE"
                else: # 닫혀있음
                    print('닫혀있음')
                    cnt = 0
                    for p in passengers:
                        i, ts, st, end = p.values()
                        if end == floor:
                            commands['commands'][id]['command'] = "OPEN"
                            cnt += 1
                    for c in calls:
                        i, ts, st, end = c.values()
                        if st == floor and len(passengers) - cnt < MAXPASS:
                            if passengers:
                                i_, ts_, st_, end_ = passengers[0].values()
                                if (end_ > floor and end > floor) or (end_ < floor and end < floor):
                                    commands['commands'][id]['command'] = "OPEN"
                                    break
                            # if elv_dir[id] == 'UP' and end > floor:
                            #     commands['commands'][id]['command'] = "OPEN"
                            #     break
                            # elif elv_dir[id] == 'DOWN' and end < floor:
                            #     commands['commands'][id]['command'] = "OPEN"
                            #     break
                    if 'command' not in commands['commands'][id]: # 내릴 승객& 탈 승객이 없습니까?
                        print('운행중 아니고 닫혀있고 내릴 승객 없음')
                        # if calls:
                        #     empty_elvs.append([id, floor])
                        # else:
                        #     print('call 없음')
                        if passengers:
                            if floor == MAXFLOOR:
                                commands['commands'][id]['command'] = 'DOWN'
                                elv_dir[id] = 'DOWN'
                            elif floor == 1:
                                commands['commands'][id]['command'] = 'UP'
                                elv_dir[id] = 'UP'
                            else:
                                i_, ts_, st_, end_ = passengers[0].values()
                                upper = False
                                below = False
                                for c in calls:
                                    i, ts, st, end = c.values()
                                    if st > floor and ((end_ > floor and end > floor) or (end_ < floor and end < floor)):
                                        upper = True
                                    if st < floor and ((end_ > floor and end > floor) or (end_ < floor and end < floor)):
                                        below = True
                                if elv_dir[id] == "UP" and upper:
                                    commands['commands'][id]['command'] = elv_dir[id]
                                elif elv_dir[id] == "DOWN" and below:
                                    commands['commands'][id]['command'] = elv_dir[id]
                                else:
                                    commands['commands'][id]['command'] = 'UP' if end_ > floor else 'DOWN'
                                    elv_dir[id] = commands['commands'][id]['command']
                                # upper = False
                                # below = False
                                # for p in passengers:
                                #     i, ts, st, end = p.values()
                                #     if end > floor:
                                #         upper = True
                                #     if end < floor:
                                #         below = True
                                # for c in calls:
                                #     i, ts, st, end = c.values()
                                #     if st > floor:
                                #         upper = True
                                #     if st < floor:
                                #         below = True
                                # if elv_dir[id] == "UP" and upper:
                                #     commands['commands'][id]['command'] = elv_dir[id]
                                # elif elv_dir[id] == "DOWN" and below:
                                #     commands['commands'][id]['command'] = elv_dir[id]
                                # else:
                                #     commands['commands'][id]['command'] = 'UP' if elv_dir[id] != "UP" else 'DOWN'
                                #     elv_dir[id] = commands['commands'][id]['command']
                        else:
                            if calls:
                                empty_elvs.append([id, floor, len(passengers)])
                            else:
                                commands['commands'][id]['command'] = 'STOP'

        print(empty_elvs)
        for c in calls:
            i, ts, st, end = c.values()
            min_d = 30
            target = -1
            tmp = []
            upper = False
            open = False
            for ev in empty_elvs:
                id, floor, passengers = ev
                if abs(st - floor) < min_d:
                    min_d = abs(st - floor)
                    f = floor
                    target = id
                    tmp = ev
                    if st > floor:
                        upper = True
                    elif st < floor:
                        upper = False
                    else:
                        if passengers < MAXPASS:
                            open = True
                            break
            if target != -1:
                if not open:
                    commands['commands'][target]['command'] = 'UP' if upper else 'DOWN'
                    elv_dir[target] = commands['commands'][target]['command']
                    # empty_elvs.remove(tmp)
                else:
                    commands['commands'][target]['command'] = 'OPEN'
                    empty_elvs.remove(tmp)

        for ev in empty_elvs:
            print(ev)
            id, floor, passengers = ev
            if 'command' in commands['commands'][id]:
                continue
            if passengers != 0: # 승객이 있다
                if floor == MAXFLOOR:
                    commands['commands'][id]['command'] = "DOWN"
                    elv_dir[id] = "DOWN"
                elif floor == 1:
                    commands['commands'][id]['command'] = "UP"
                    elv_dir[id] = "UP"
                else:
                    commands['commands'][id]['command'] = elv_dir[id]
            else:
                if id == 0:
                    first = True
                commands['commands'][ev[0]]['command'] = "STOP"

        print(calls)
        print(elevators)
        print(commands)
        action(token, commands)


simulate()