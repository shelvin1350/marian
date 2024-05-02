from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def attendance_register(request):
    data = {
        'details':[
    {"slno": "1", "name": "Zvbejsr"},
    {"slno": "2", "name": "Fzqslbd"},
    {"slno": "3", "name": "Vupsmhn"},
    {"slno": "4", "name": "Qilxrug"},
    {"slno": "5", "name": "Lmzptkr"},
    {"slno": "6", "name": "Jnmkflw"},
    {"slno": "7", "name": "Ibgoymt"},
    {"slno": "8", "name": "Rtskbey"},
    {"slno": "9", "name": "Vtawdjx"},
    {"slno": "10", "name": "Yvdfbke"},
    {"slno": "11", "name": "Udwxygl"},
    {"slno": "12", "name": "Ergvlhm"},
    {"slno": "13", "name": "Ckayomt"},
    {"slno": "14", "name": "Ycvwxop"},
    {"slno": "15", "name": "Xflieav"},
    {"slno": "16", "name": "Xysuebc"},
    {"slno": "17", "name": "Kybqxnz"},
    {"slno": "18", "name": "Zlubmiv"},
    {"slno": "19", "name": "Oarblze"},
    {"slno": "20", "name": "Jufqpew"},
    {"slno": "21", "name": "Amszkxl"},
    {"slno": "22", "name": "Jdqfglz"},
    {"slno": "23", "name": "Dyqhlof"},
    {"slno": "24", "name": "Pvwiqna"},
    {"slno": "25", "name": "Ouqzmpt"},
    {"slno": "26", "name": "Vtbdwln"},
    {"slno": "27", "name": "Xefqugo"},
    {"slno": "28", "name": "Gvoymjc"},
    {"slno": "29", "name": "Ugyjekm"},
    {"slno": "30", "name": "Iefqtcv"},
    {"slno": "31", "name": "Cynxdha"},
    {"slno": "32", "name": "Mqjwxfd"},
    {"slno": "33", "name": "Lxzbrgn"},
    {"slno": "34", "name": "Kqmwjup"},
    {"slno": "35", "name": "Wlzmpki"},
    {"slno": "36", "name": "Wpeblnd"},
    {"slno": "37", "name": "Wrfvhml"},
    {"slno": "38", "name": "Kneuiwy"},
    {"slno": "39", "name": "Scjdlru"},
    {"slno": "40", "name": "Cqlebfm"},
    {"slno": "41", "name": "Nfclqge"},
    {"slno": "42", "name": "Azlgtiw"},
    {"slno": "43", "name": "Ebfkjlc"},
    {"slno": "44", "name": "Ovnyfjd"},
    {"slno": "45", "name": "Gnvexcl"},
    {"slno": "46", "name": "Bvlekyi"},
    {"slno": "47", "name": "Gvbzltm"},
    {"slno": "48", "name": "Fgbhljk"},
    {"slno": "49", "name": "Qowepbv"},
    {"slno": "50", "name": "Vwxotyl"}
]
    }
    return render(request, 'attendance_register.html', data)