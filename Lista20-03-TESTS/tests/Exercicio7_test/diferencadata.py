from datetime import datetime

def diferenca_entre_datas(data1, data2, unidade="dias"):
    formato_data = "%Y-%m-%d %H:%M" if " " in data1 else "%Y-%m-%d"
    data1 = datetime.strptime(data1, formato_data)
    data2 = datetime.strptime(data2, formato_data)
    diferenca = abs(data2 - data1)
    
    if unidade == "dias":
        return diferenca.days
    elif unidade == "meses":
        return round(diferenca.days / 30)
    elif unidade == "anos":
        return round(diferenca.days / 365)
    elif unidade == "horas":
        return diferenca.total_seconds() / 3600
    elif unidade == "minutos":
        return diferenca.total_seconds() / 60
