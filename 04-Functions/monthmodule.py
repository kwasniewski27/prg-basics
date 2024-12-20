def month(n):
    months = {
        1 : "Styczeń",
        2 : "Luty",
        3 : "Marzec",
        4 : "Kwiecień",
        5 : "Maj",
        6 : "Czerwiec",
        7 : "Lipiec",
        8 : "Sierpień",
        9 : "Wrzesień",
        10 : "Pażdziernik",
        11 : "Listopad",
        12 : "Grudzień"
    }
    return months.get(n, "Invalid month number")