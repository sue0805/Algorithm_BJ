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
    elvs = ["UP"] * 4

    while not is_end:
        t, ts, elevators, calls, is_end = call(token).values()
        check = defaultdict(bool)
        commands = {'commands' : [{} for i in range(4)]}
        print(calls)
        print(elevators)
        for ev in elevators:
            id, floor, passengers, status = ev.values()
            commands['commands'][id]["elevator_id"] = id
            if status == 'STOPPED':
                if len(calls) == 0:
                    commands['commands'][id]["command"] = "STOP"
                if not passengers:
                    tmp = "STOP"
                    for c in calls:
                        i, ts, st, end = c.values()
                        if check[(i, ts)]:
                            continue
                        if st == floor:
                            commands['commands'][id]["command"] = "OPEN"
                            check[(i, ts)] = True
                            break
                        elif st > floor:
                            tmp = "UP"
                            elvs[id] = tmp
                        elif st < floor:
                            tmp = "DOWN"
                            elvs[id] = tmp

                    if 'command' not in commands['commands'][id]:
                        commands['commands'][id]['command'] = tmp
                        elvs[id] = 'UP' if elvs[id] == 'DOWN' else 'DOWN'
                else:
                    tmp = [(abs(floor - p['end']), p['end'] > floor) for p in passengers]
                    goal = min(tmp)
                    print(goal)
                    if goal[1]:
                        commands['commands'][id]['command'] = "UP"
                    elif goal[0] == 0:
                        commands['commands'][id]['command'] = "OPEN"
                    else:
                        commands['commands'][id]['command'] = "DOWN"

            elif status == 'OPENED':
                commands['commands'][id]["call_ids"] = []
                for p in passengers:
                    i, ts, st, end = p.values()
                    if end == floor:
                        commands['commands'][id]["call_ids"].append(i)
                if commands['commands'][id]["call_ids"]:
                    commands['commands'][id]["command"] = "EXIT"
                    continue
                tmp = []
                for c in calls:
                    i, ts, st, end = c.values()
                    if st == floor:
                        if len(commands['commands'][id]["call_ids"]) + len(passengers) == MAXPASS:
                            break
                        commands['commands'][id]["call_ids"].append(i)
                        tmp.append(c)
                while tmp:
                    calls.remove(tmp.pop())
                    print('removal!')
                    print(calls)
                if commands['commands'][id]["call_ids"]:
                    commands['commands'][id]["command"] = "ENTER"
                    continue
                else:
                    commands['commands'][id]["command"] = "CLOSE"
            elif status.startswith("UP"):
                for p in passengers:
                    i, ts, st, end = p.values()
                    if end == floor:
                        commands['commands'][id]["command"] = "STOP"
                        break
                for c in calls:
                    i, ts, st, end = c.values()
                    if st == floor:
                        commands['commands'][id]['command'] = "STOP"
                        break
                if floor == MAXFLOOR:
                    commands['commands'][id]["command"] = "STOP"
                    elvs[id] = "DOWN"
                if 'command' not in commands['commands'][id]:
                    commands['commands'][id]["command"] = "UP"
            elif status.startswith("DOWN"):
                for p in passengers:
                    i, ts, st, end = p.values()
                    if end == floor:
                        commands['commands'][id]["command"] = "STOP"
                        break
                for c in calls:
                    i, ts, st, end = c.values()
                    if st == floor:
                        commands['commands'][id]['command'] = "STOP"
                        break
                if floor == 1:
                    commands['commands'][id]["command"] = "STOP"
                    elvs[id] = "UP"
                if 'command' not in commands['commands'][id]:
                    commands['commands'][id]["command"] = "DOWN"
        print(elvs)
        print(commands)
        action(token, commands)


simulate()