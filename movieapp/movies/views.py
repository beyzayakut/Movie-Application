from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Category, Movie

kategori_liste = ["Macera", "Romantik", "Dram", "Aksiyon", "Bilim Kurgu"]
film_liste = [
    {
        "id": 1,
        "film_adi": "Titanic",
        "aciklama": "İnsan elinden çıkmış en büyük ve en gösterişli yüzen araç olan Titanic yola koyuldu. Batmaz, sarsılmaz denilen bu büyük lüks yolcu gemisinde yolculuk yapmak, 20. Yüzyılın muhteşem bir rüyasıydı. Ancak bu büyük rüya sadece 4.5 gün serecek ve anısını bir sonraki yüzyıla bile taşıyacak büyüklükte bir kabusa dönüşecekti.",
        "resim": "1.jpeg",
        "anasayfa": True
    },
    {
        "id": 2,
        "film_adi": "V For Vendatte",
        "aciklama": "V olarak bilinen maskeli bir adam, geleceğin totaliter rejimle yönetilen İngilteresi'nde korkuyla sindirilmiş halkına egemenliği geri verebilmek için şiddete başvuran biridir. V İngiltere halkını, kendisiyle Guy Fawkes günü olan 5 Kasım’da Parlamento’nun çevresinde buluşmaya davet eder.",
        "resim": "2.jpeg",
        "anasayfa": True
    },
    {
        "id": 3,
        "film_adi": "Forrest Gump",
        "aciklama": "Forrest Gump, zeka seviyesi 75 olan bir erkeğin hayatını ele alıyor. Zeka seviyesi nedeni ile devlet okullarına girmekte bile zorlanan Forrest Gump zamanla akla mantığa uymayan başarılara imza atıyor. Her ne kadar zeka seviyesi düşük olsa da fiziksel olarak son derece sağlam olan Forrest Gump, zamanla gelişen olaylar zincirinde bizi hayal edemeyeceğimiz bir dünyaya götürüyor.",
        "resim": "3.jpeg",
        "anasayfa": True
    },
    {
        "id": 4,
        "film_adi": "Akıl Oyunları",
        "aciklama": "John Forbes Nash Jr., genç yaşında geliştirdiği kuramlarla matematik dünyasının bir numaralı ismi haline gelir. Fakat kısa süre içerisinde bencilliği ve kendine olan aşırı güveni sonucunda oluşan kişisel problemleri ile baş edemez duruma düşer. Dahilik ile delilik arasındaki ince çizgide, delilik tarafına doğru sürüklenir.",
        "resim": "4.jpeg",
        "anasayfa": True
    }
]

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all() 
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    try:
        film = next(film for film in film_liste if film["id"] == id)
    except StopIteration:
        raise Http404("Film bulunamadı")
    
    data = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, "details.html", data)
