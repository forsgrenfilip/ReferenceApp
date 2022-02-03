# -*- coding: utf-8 -*-p
def go():
    from datetime import datetime

    string_input_with_date = "30/09/2021"
    end = datetime.strptime(string_input_with_date, "%d/%m/%Y")
    present = datetime.now()

    if end.date() < present.date():
        return 0
    else:
        return 1