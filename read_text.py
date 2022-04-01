from gtts import gTTS
from io import BytesIO
import pygame
import time



def speak(text, language='en'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    x = pygame.mixer.music.load(mp3_fo, 'mp3')

    pygame.mixer.music.play()



pygame.init()
pygame.mixer.init()
# sound.seek(0)

 
slides = """Cos'è il budget?
Il budget è il documento di natura contabile che contiene le previsioni e gli obiettivi per il prossimo esercizio. Si tratta di dati basati su delle stime,
quindi è un documento preventivo, al contrario del bilancio che è un documento consuntivo e non è obbligatorio.
Come si articola il budget?

Si articola per unità organizzative dette centri di responsabilità che sono affidate ad un manager,
cui vengono assegnate risorse e obiettivi da raggiungere.

Tipi di budget:

budget incrementativo:
si fanno previsioni in aumento o diminuzione rispetto ai dati dell’anno precedente.

budget scorrevole:
si divide l'anno in periodi;
al termine di ciascun periodo lo si analizza  e poi si aggiunge una nuova previsione per un altro periodo successivo all'ultimo in modo da avere sempre un budget proiettato su un anno.

- budget flessibile: 
prevede tre scenari: uno favorevole, uno stabile e uno sfavorevole.

- budget a base zero: 
rialloca le risorse e rivede gli obiettivi senza tener conto delle previsioni fatte in precedenza, ripartendo, appunto, da zero.

Il budget si basa sui costi standard

I costi standard sono costi di riferimento che servono a controllarne l’andamento e il loro impatto sull'utile dell'impresa.

I costi standard possono essere:
- correnti: sono quelli attuali;

- ottenibili: 
sono più bassi di quelli correnti, raggiungibili con una maggiore efficienza nell’impiego dei fattori produttivi.
Vengono usati come obiettivo da raggiungere, perché stimolano l'azienda a migliorare, senza risultare troppo difficili da raggiungere.

- ideali: 
sono costi molto bassi che prevedono il massimo di efficienza e sprechi ridotti al minimo, perciò sono difficili da raggiungere e non si pongono come obiettivi.

Come si articola il budget?

Il budget è composto da:
- budget degli investimenti: 
prevede gli acquisti e le dismissioni delle immobilizzazioni

- Budget economico: 
prevede i costi e i ricavi del prossimo esercizio

- Budget finanziario:
presenta la composizione delle fonti di finanziamento

- Budget di esercizio: riepiloga i dati degli altri budget

Budget economico di un ristorante

Facciamo una breve sintesi del processo per redigere il budget economico di un ristorante

Si parte dalla previsione dei coperti che saranno venduti nell'anno successivo.

Otteniamo i ricavi previsti moltiplicando i coperti per il loro prezzo previsto.

Si calcolano anche i costi delle materie prime e della manodopera in base alle vendite previste.
Infine si calcolano gli altri costi di produzione, gli interessi passivi e le imposte per ottenere l'utile previsto,

Controllo budgetario
È il controllo effettuato mettendo a confronto i dati effettivi con i dati previsti.
Ci possono essere degli scostamenti nei ricavi o nei costi per effetto di variazioni nei prezzi di vendita o di acquisto, oppure delle variazioni nei rendimenti dei fattori produttivi.
Se sono significativi occorre indagare sulle possibili cause.

Il controllo budgetario si conclude con un rapporto informativo per l'alta direzione perpermettere loro di prendere le decisioni per cercare di riportare l'impresa verso gli obiettivi programmati.
""".splitlines()

def speak(text=" ", language='it'):

    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    pygame.mixer.music.load(mp3_fo, 'mp3')
    pygame.mixer.music.play()


for slide in slides:
    if slide != "":
        speak(slide)
        time.sleep(len(slide.split(" "))/2)







