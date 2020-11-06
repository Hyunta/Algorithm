def solution(time, plans):
    last = ""
    for plan in plans:
        city, start, end = plan

        start_time, start_style = get_time_style(start)
        end_time, end_style = get_time_style(end)

        start_time = convert_time(start_time, start_style)
        end_time = convert_time(end_time, end_style)

        loss = calculate_loss(start_time, end_time)
        if time - loss < 0:
            break
        last = city

    return last


def get_time_style(given):
    time = int(given[:-2])
    style = given[-2:]
    return time, style


def calculate_loss(start_time, end_time):
    loss = 0
    company_start = 9.5
    company_end = 18
    mon_company_start = 13

    if start_time <= company_start:
        loss += 8.5
    elif company_start < start_time <= company_end:
        loss += company_end - start_time

    if mon_company_start <= end_time < company_end:
        loss += end_time - mon_company_start
    elif end_time >= company_end:
        loss += 5

    return loss


def convert_time(time, style):
    if style == "PM":
        time = 12 + time
    if time == 12 and style == "AM":
        time = 0
    return time


print(solution(3.5, [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]]))
