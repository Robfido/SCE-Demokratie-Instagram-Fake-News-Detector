from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    validity = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Chanel %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    init_db()
    if request.method == 'POST':
        search_name = request.form['channel_name']
        return redirect(f'/search/{search_name}')
        # search_result = Channel.query.filter_by(name=search_name).order_by(Channel.id).all()
    else:
        #tasks = Channel.query.order_by(Channel.id).all()
        return render_template('index.html')
        #return render_template('index.html', tasks=tasks)     

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         task_content = request.form['channel_name']
#         new_task = Todo(content=task_content)

#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue adding your task'

#     else:
#         tasks = Todo.query.order_by(Todo.id).all()
#         return render_template('index.html', tasks=tasks)

@app.route('/ueberuns/')
def show_ueber_uns():
    #ret_value = Channel.query.filter_by(channel_name="bild").all()
    return render_template('ueberuns.html')


@app.route('/search/')
def empty_search():
    return redirect('/')

@app.route('/search/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    #if subpath in valid_content_dict.keys():
    ret_value = Channel.query.filter_by(channel_name=subpath).all()#.order_by(Channel.id).all()
    print('######################################################################################################')
    print(ret_value)
    #print(ret_value[0].channel_name)
    #print(Channel.query.filter_by(channel_name="ard").one())
    if len(ret_value) == 1:
        return render_template('index.html', channel=ret_value, notfound=False)
    #     ret_value = valid_content_dict[subpath]
    # elif subpath in not_valid_content_dict.keys():
    #     ret_value = not_valid_content_dict[subpath]
    # elif subpath in satire_content_dict.keys():
    #     ret_value = satire_content_dict[subpath]
    else:
        return render_template('index.html', channel=[], notfound=True)
    #return f'Subpath {escape(subpath)}'
    #return ret_value




# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)

#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task'

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)

#     if request.method == 'POST':
#         task.content = request.form['content']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your task'

#     else:
#         return render_template('update.html', task=task)



def init_db():
    trustedSourcesDict = {
    "tagesschau": "Der Tagesschau Instagram-Kanal wird als seriös eingestuft, da er von einer etablierten und respektierten Nachrichtenorganisation betrieben wird, die seit Jahrzehnten für ihre gründliche und objektive Berichterstattung bekannt ist. Zudem werden auf dem Kanal aktuelle und verifizierte Informationen geteilt, die von professionellen Journalisten sorgfältig recherchiert und präsentiert werden. Schließlich trägt die Einhaltung journalistischer Standards und ethischer Richtlinien dazu bei, das Vertrauen der Nutzer in die Genauigkeit und Zuverlässigkeit der bereitgestellten Inhalte zu stärken.",
    "sportschau": "Der Sportschau Instagram-Kanal wird als seriös eingestuft, da er von der ARD betrieben wird, einer renommierten öffentlich-rechtlichen Rundfunkanstalt mit einem hohen journalistischen Standard. Der Kanal liefert aktuelle und detaillierte Berichterstattung über Sportereignisse, die von erfahrenen Sportjournalisten recherchiert und präsentiert werden. Zudem sorgt die transparente und faktenbasierte Darstellung von Informationen für Vertrauen und Glaubwürdigkeit bei den Nutzern.",
    "bericht.aus.berlin": "Der Bericht aus Berlin Instagram-Kanal wird als seriös eingestuft, da er von der ARD betrieben wird, einer anerkannten öffentlich-rechtlichen Rundfunkanstalt, die für hochwertige und unabhängige Berichterstattung steht. Der Kanal bietet fundierte Analysen und Hintergrundberichte zu politischen Entwicklungen in Deutschland, die von erfahrenen Journalisten sorgfältig recherchiert und verständlich aufbereitet werden. Zudem gewährleistet die Einhaltung journalistischer Standards und ethischer Richtlinien die Glaubwürdigkeit und Zuverlässigkeit der veröffentlichten Inhalte.",
    "weltspiegel":  "Der Weltspiegel Instagram-Kanal wird als seriös eingestuft, da er von der ARD betrieben wird, einer öffentlich-rechtlichen Rundfunkanstalt mit langjähriger Erfahrung und einem hohen journalistischen Standard. Der Kanal bietet tiefgehende und gut recherchierte internationale Berichterstattung, die von erfahrenen Korrespondenten vor Ort erstellt wird. Die Einhaltung ethischer Standards und die transparente Informationsvermittlung tragen ebenfalls zur Glaubwürdigkeit und Zuverlässigkeit des Kanals bei.",
    "zdfheute":  "Der ZDFheute Instagram-Kanal wird als seriös eingestuft, da er von der renommierten öffentlich-rechtlichen Rundfunkanstalt ZDF betrieben wird, die für ihre fundierte und unabhängige Berichterstattung bekannt ist. Der Kanal liefert aktuelle Nachrichten und gründlich recherchierte Informationen, die von professionellen Journalisten erstellt und überprüft werden. Zudem sorgt die Einhaltung journalistischer Standards und die objektive Präsentation von Inhalten für hohe Glaubwürdigkeit und Verlässlichkeit bei den Nutzern.",
    "spiegelmagazin": "Der Spiegel Magazin Instagram-Kanal wird als seriös eingestuft, da er von der etablierten und bekannten Nachrichtenzeitschrift Der Spiegel betrieben wird, die für ihre investigative und sorgfältig recherchierte Berichterstattung bekannt ist. Der Kanal liefert fundierte Analysen und aktuelle Informationen, die von erfahrenen Journalisten erstellt und überprüft werden. Zudem trägt die Einhaltung journalistischer Standards und die Transparenz in der Informationsvermittlung zur hohen Glaubwürdigkeit und Zuverlässigkeit des Kanals bei.",
    "sz": "Der Instagram-Kanal der Süddeutschen Zeitung wird als seriös eingestuft, da er von einer der führenden und renommiertesten Tageszeitungen Deutschlands betrieben wird, die für ihre tiefgehende und investigative Berichterstattung bekannt ist. Auf dem Kanal werden sorgfältig recherchierte Nachrichten und Analysen veröffentlicht, die von erfahrenen Journalisten erstellt und überprüft werden. Zudem sorgt die konsequente Einhaltung journalistischer Standards und ethischer Richtlinien für Glaubwürdigkeit und Vertrauen bei den Nutzern.",
    "deutschlandfunk": "Der Deutschlandfunk Instagram-Kanal wird als seriös eingestuft, da er von einer renommierten öffentlich-rechtlichen Rundfunkanstalt betrieben wird, die für unabhängige und fundierte Berichterstattung bekannt ist. Der Kanal bietet aktuelle Nachrichten und tiefgehende Analysen, die von erfahrenen Journalisten sorgfältig recherchiert und geprüft werden. Zudem trägt die Einhaltung hoher journalistischer Standards und ethischer Richtlinien zur Glaubwürdigkeit und Verlässlichkeit der bereitgestellten Inhalte bei.",
    "br24": "Der BR24 Instagram-Kanal wird als seriös eingestuft, da er von Bayerischem Rundfunk betrieben wird, einer anerkannten öffentlich-rechtlichen Rundfunkanstalt mit einem hohen journalistischen Standard. Der Kanal bietet aktuelle und gründlich recherchierte Informationen, die von erfahrenen Journalisten erstellt und überprüft werden. Außerdem trägt die konsequente Einhaltung journalistischer Ethik und die transparente Berichterstattung zur Glaubwürdigkeit und Verlässlichkeit der Inhalte bei.",
    "ndrniedersachsen": "Der NDR Niedersachsen Instagram-Kanal wird als seriös eingestuft, da er von einer der öffentlich-rechtlichen Rundfunkanstalten, dem Norddeutschen Rundfunk (NDR), betrieben wird, die für ihre qualitativ hochwertige und unabhängige Berichterstattung bekannt ist. Der Kanal liefert relevante und gut recherchierte Nachrichten aus der Region Niedersachsen, die von erfahrenen Journalisten sorgfältig geprüft werden. Zudem trägt die Einhaltung hoher journalistischer Standards und ethischer Richtlinien zur Glaubwürdigkeit und Verlässlichkeit der veröffentlichten Inhalte bei.",
    "swraktuell": "Der SWR Aktuell Instagram-Kanal wird als seriös eingestuft, da er von dem Südwestrundfunk (SWR), einer anerkannten öffentlich-rechtlichen Rundfunkanstalt mit hohem journalistischem Standard, betrieben wird. Der Kanal bietet aktuelle und präzise Nachrichten, die von erfahrenen Journalisten gründlich recherchiert und überprüft werden. Zudem stärkt die konsequente Einhaltung journalistischer Ethik und die transparente Berichterstattung die Glaubwürdigkeit und Verlässlichkeit der veröffentlichten Inhalte.",
    "arte.tv": "Der ARTE.tv Instagram-Kanal wird als seriös eingestuft, da er von ARTE, einem renommierten öffentlich-rechtlichen europäischen Kultursender, betrieben wird, der für seine hochwertigen und gut recherchierten Inhalte bekannt ist. Der Kanal bietet qualitativ hochwertige Beiträge zu kulturellen, gesellschaftlichen und politischen Themen, die von professionellen Journalisten und Experten sorgfältig erstellt und überprüft werden. Zudem sorgt die Einhaltung hoher journalistischer und ethischer Standards sowie die transparente Darstellungsweise für Vertrauen und Glaubwürdigkeit bei den Nutzern.",
    "ard": "Der ARD Instagram-Kanal wird als seriös eingestuft, weil er von einer der größten und angesehensten öffentlich-rechtlichen Rundfunkanstalten Deutschlands betrieben wird, was für Qualität und Glaubwürdigkeit spricht. Die Inhalte auf dem Kanal sind gut recherchiert und basieren auf journalistischen Standards, die Transparenz und Fakten als oberste Priorität haben. Zudem werden regelmäßig Nachrichten, Hintergrundberichte und aktuelle Informationen geteilt, die eine breite und kritische Informationsbasis bieten.",
    "bbcnews": "Der BBC News Instagram-Kanal gilt als seriös, da er von der British Broadcasting Corporation betrieben wird, einer weltweit renommierten Nachrichtenorganisation mit einem hohen journalistischen Standard. Die Beiträge sind gut recherchiert und ausgeglichen, basierend auf Fakten und umfassender Berichterstattung, was Transparenz und Glaubwürdigkeit gewährleistet. Außerdem bietet der Kanal aktuelle Nachrichten, Hintergrundinformationen und detaillierte Analysen, die das Vertrauen der Nutzer in die Qualität und Zuverlässigkeit der Informationen stärken.",
    "bbc": "Der BBC Instagram-Kanal wird als seriös eingestuft, weil die BBC eine weltweit anerkannte und respektierte Nachrichtenorganisation ist, die für ihre unabhängige und objektive Berichterstattung bekannt ist. Die auf dem Kanal veröffentlichten Inhalte sind sorgfältig recherchiert und basieren auf verifizierten Informationen, die den hohen journalistischen Standards entsprechen. Zudem behandelt der Kanal eine breite Palette von Themen, bietet aktuelle Nachrichten und fundierte Analysen, wodurch er als verlässliche Informationsquelle geschätzt wird.",
    "cnn": "Der CNN Instagram-Kanal wird als seriös eingestuft, da er von einer führenden globalen Nachrichtenorganisation betrieben wird, die für ihre umfangreiche und fundierte Berichterstattung weltweit bekannt ist. Die Inhalte auf dem Kanal sind gut recherchiert, basieren auf verifizierten Informationen und folgen hohen journalistischen Standards, was Transparenz und Genauigkeit sicherstellt. Zudem bietet der Kanal aktuelle Nachrichten und detaillierte Analysen zu verschiedenen Themen, was ihn zu einer verlässlichen Informationsquelle für seine Nutzer macht.",
    "cnnpolitics": "Der CNN Politics Instagram-Kanal wird als seriös eingestuft, da er von einer renommierten Nachrichtenorganisation betrieben wird, die für ihre tiefgehende politische Berichterstattung bekannt ist. Die Inhalte sind gut recherchiert, basieren auf verifizierten Informationen und folgen strengen journalistischen Standards, was Glaubwürdigkeit und Objektivität sicherstellt. Darüber hinaus bietet der Kanal eine breite Palette an aktuellen politischen Nachrichten, Analysen und Hintergrundinformationen, die eine kritische und fundierte Auseinandersetzung mit politischen Themen ermöglichen.",
    "nbcnews": "Der NBC News Instagram-Kanal wird als seriös eingestuft, da er von einer etablierten und angesehenen Nachrichtenorganisation betrieben wird, die für ihre umfassende und zuverlässige Berichterstattung bekannt ist. Die geposteten Inhalte sind sorgfältig recherchiert, basieren auf verifizierten Informationen und folgen hohen journalistischen Standards, was Vertrauen und Integrität gewährleistet. Zudem deckt der Kanal ein breites Spektrum aktueller Nachrichten und Analysen ab, wodurch die Nutzer stets gut informiert sind.",
    "nytimes": "Der New York Times Instagram-Kanal wird als seriös eingestuft, weil er von einer der weltweit angesehensten und ältesten Nachrichtenorganisationen betrieben wird, die für ihre gründlichen Recherchen und hochwertigen journalistischen Standards bekannt ist. Die Inhalte sind stets gut recherchiert und basieren auf verifizierten Fakten, was Transparenz und Vertrauenswürdigkeit sicherstellt. Darüber hinaus bietet der Kanal eine breite Palette an aktuellen Nachrichten, tiefgehenden Analysen und Hintergrundinformationen, was ihn zu einer verlässlichen Quelle für seine Nutzer macht.",
    "washingtonpost": "Der Washington Post Instagram-Kanal wird als seriös eingestuft, weil er von einer etablierten und renommierten Nachrichtenorganisation betrieben wird, die für ihre investigative Berichterstattung und hohen journalistischen Standards bekannt ist. Die veröffentlichten Inhalte sind sorgfältig recherchiert, basieren auf verifizierten Fakten und gewährleisten somit Transparenz und Glaubwürdigkeit. Zudem bietet der Kanal eine umfassende Berichterstattung aktueller Nachrichten und tiefgehender Analysen, wodurch er eine verlässliche Informationsquelle für seine Nutzer darstellt.",
    "guardian": "Der Guardian Instagram-Kanal wird als seriös eingestuft, weil er von einer angesehenen Nachrichtenorganisation betrieben wird, die für ihren unabhängigen und investigativen Journalismus bekannt ist. Die Inhalte auf dem Kanal sind sorgfältig recherchiert, basieren auf verifizierten Informationen und folgen strengen journalistischen Standards, was Glaubwürdigkeit und Transparenz sicherstellt. Darüber hinaus deckt der Kanal eine breite Palette aktueller Nachrichten, Analysen und Hintergrundgeschichten ab, wodurch er als verlässliche Informationsquelle geschätzt wird.",
    "faz": "Der FAZ Instagram-Kanal wird als seriös eingestuft, weil er von der Frankfurter Allgemeinen Zeitung betrieben wird, einer renommierten deutschen Tageszeitung, die für ihre gründliche Recherche und hohen journalistischen Standards bekannt ist. Die veröffentlichten Inhalte sind objektiv, gut recherchiert und basieren auf verifizierten Fakten, was Transparenz und Glaubwürdigkeit sicherstellt. Zudem bietet der Kanal eine breite Palette an aktuellen Nachrichten, tiefgehenden Analysen und Hintergrundinformationen, wodurch er eine verlässliche Informationsquelle für seine Nutzer darstellt.",
    "ardmediathek": "Der ARD Mediathek Instagram-Kanal wird als seriös eingestuft, weil er durch die ARD, einen etablierten öffentlich-rechtlichen Rundfunkdienst in Deutschland, betrieben wird, was Sicherheit und Verlässlichkeit seiner Inhalte garantiert. Der Kanal bietet hochwertige, gut recherchierte Informationen und Nachrichteninhalte, die den journalistischen Standards der ARD entsprechen. Zudem werden keine irreführenden oder sensationsheischenden Beiträge geteilt, was die Vertrauenswürdigkeit und Seriosität des Kanals unterstützt."
    }
    untrustedSourcesDict = {
    "foxnews": "Der Fox News Instagram-Kanal wird als nicht seriös eingestuft, da die Berichterstattung der Muttergesellschaft häufig als voreingenommen und politisch parteiisch kritisiert wird. Zudem wird dem Kanal vorgeworfen, gelegentlich unzureichend verifizierte oder übermäßig sensationelle Informationen zu verbreiten, was die Glaubwürdigkeit unterminiert. Infolgedessen zweifeln viele Nutzer an der Objektivität und Genauigkeit der präsentierten Inhalte, was das Vertrauen in den Kanal beeinträchtigt.",
    "bild": "Der BILD Instagram-Kanal wird als nicht seriös eingestuft, weil die Inhalte häufig reißerisch und sensationsorientiert aufbereitet sind, was die journalistische Qualität beeinträchtigt. Zudem wird BILD vorgeworfen, manchmal ungenau oder voreilig zu berichten, was zu Fehlinformationen führen kann. Die starke Fokussierung auf populäre Themen und teilweise kontroverse Berichterstattung erweckt bei vielen Nutzern den Eindruck von mangelnder Objektivität und fundierter Recherche.",
    "afd.bund": "Der Instagram-Kanal der AfD (afd.bund) wird als nicht seriös eingestuft, weil die Inhalte häufig stark politisch gefärbt und parteiisch sind, was eine objektive Berichterstattung ausschließt. Zudem wird dem Kanal vorgeworfen, Desinformationen und populistische Botschaften zu verbreiten, die wissenschaftlich nicht immer fundiert sind. Die kontroverse und polarisierende Art der Kommunikation trägt zusätzlich dazu bei, dass viele Nutzer die Inhalte als unzuverlässig und tendenziös wahrnehmen.",
    "afdimbundestag": "Der Instagram-Kanal der AfD im Bundestag (afdimbundestag) wird als nicht seriös eingestuft, weil die Inhalte häufig stark ideologisch geprägt und politisch einseitig sind, was die Objektivität infrage stellt. Zusätzlich wird dem Kanal vorgeworfen, gelegentlich Desinformationen und populistische Aussagen zu verbreiten, die nicht auf wissenschaftlichen Fakten basieren. Die Kommunikation ist oft provokativ und polarisierend, was das Vertrauen in die Zuverlässigkeit und Neutralität der präsentierten Informationen mindert.",
    "rt": "Der RT (Russia Today) Instagram-Kanal wird als nicht seriös eingestuft, weil er von einer staatlich kontrollierten russischen Nachrichtenorganisation betrieben wird, die häufig Propaganda und politisch motivierte Inhalte verbreitet. Die Berichterstattung ist oft einseitig und verzerrt, was die Objektivität und journalistische Integrität untergräbt. Zudem wird RT vorgeworfen, Desinformationen und Verschwörungstheorien zu fördern, was das Vertrauen in die Zuverlässigkeit und Glaubwürdigkeit des Kanals stark beeinträchtigt.",
    "welt": "Der WELT Kanal ist nicht seriös, weil die Berichterstattung oft als sensationsgierig und reißerisch wahrgenommen wird, was die Glaubwürdigkeit untergräbt. Kritiker bemängeln, dass manche Inhalte oberflächlich recherchiert und nicht immer objektiv dargestellt werden. Zudem wird dem Kanal vorgeworfen, eine einseitige Sichtweise zu fördern und kontroverse Themen übermäßig zu betonen, was die journalistische Integrität in Frage stellt."
    }
    satireDict = {
    "realpostillon": "Der realpostillon Instagram-Kanal wird als Satire eingestuft, da er regelmäßig humorvolle und übertriebene Nachrichten veröffentlicht, die bewusst absurde und fiktive Elemente enthalten. Die Inhalte sind darauf ausgelegt, gesellschaftliche Themen und aktuelle Ereignisse auf humorvolle Weise zu kommentieren und zu überspitzen, um zum Nachdenken und Lachen anzuregen. Zudem ist der Postillon als Satire- und Humorplattform weithin bekannt, was die Absicht hinter ihren Beiträgen für die meisten Nutzer klar erkennbar macht.",
    "theonion": "Der The Onion Instagram-Kanal wird als Satire eingestuft, weil er regelmäßig humorvolle und absurde Nachrichtenbeiträge veröffentlicht, die fiktiv und übertrieben sind. Die Inhalte zielen darauf ab, aktuelle Ereignisse und gesellschaftliche Themen auf eine ironische und oft paradoxe Weise darzustellen, um sowohl zu unterhalten als auch zu reflektieren. Zudem ist The Onion als eine der bekanntesten Satire-Nachrichtenquellen international bekannt, was die satirische Natur ihrer Beiträge für die meisten Nutzer eindeutig macht.",
    "thebabylonbee": "Der The Babylon Bee Instagram-Kanal wird als Satire eingestuft, weil er regelmäßig humorvolle und erfundene Nachrichtenbeiträge veröffentlicht, die bewusst absurde und übertriebene Darstellungen von realen Ereignissen und Themen enthalten. Die Inhalte parodieren oft aktuelle politische und gesellschaftliche Entwicklungen, um auf unterhaltsame Weise kritische Kommentare abzugeben und das Publikum zum Lachen zu bringen. Zudem ist The Babylon Bee als satirische Nachrichtenquelle weithin bekannt, was die satirische Absicht ihrer Beiträge für die meisten Nutzer klar erkennbar macht.",
    "heuteshow": "Der heute-show Instagram-Kanal wird als Satire eingestuft, weil er regelmäßig humorvolle und überzeichnete Beiträge veröffentlicht, die politische und gesellschaftliche Ereignisse auf eine ironische Weise darstellen. Die Inhalte zielen darauf ab, aktuelle Themen durch Übertreibung und Parodie zu kommentieren, um sowohl zum Lachen anzuregen als auch kritische Reflexion zu fördern. Zudem ist die heute-show als eine der bekanntesten Satire-Sendungen im deutschen Fernsehen bekannt, was die satirische Natur ihrer Beiträge für die meisten Nutzer eindeutig macht.",
    "martinhsonneborn": "Der Martin Sonneborn Instagram-Kanal wird als Satire eingestuft, weil er regelmäßig humorvolle und ironische Beiträge veröffentlicht, die politische und gesellschaftliche Themen auf eine übertriebene und oft absurde Weise kommentieren. Martin Sonneborn, als Gründer der PARTEI und bekannter Satiriker, nutzt den Kanal, um durch Parodie und Sarkasmus auf Missstände und aktuelle Ereignisse aufmerksam zu machen. Seine Inhalte sind bewusst provokativ und überspitzt, was deutlich macht, dass sie satirischer Natur sind und nicht wörtlich genommen werden sollten.",
    "extra3": "Der extra3 Instagram-Kanal wird als Satire eingestuft, weil er regelmäßig humorvolle und zugespitzte Beiträge veröffentlicht, die aktuelle politische und gesellschaftliche Ereignisse auf ironische Weise kommentieren. Die Inhalte sind oft übertrieben und parodistisch gestaltet, um Missstände und Absurditäten in verschiedenen Bereichen aufzudecken und damit zum Nachdenken anzuregen. Zudem ist extra3 als eine der bekanntesten Satire-Sendungen im deutschen Fernsehen bekannt, was die satirische Intention ihrer Beiträge für die meisten Nutzer klar erkennbar macht.",
    "titanicmagazin": "Der Titanic Magazin Instagram-Kanal wird als Satire eingestuft, weil er regelmäßig provokante und ironische Beiträge veröffentlicht, die politische und gesellschaftliche Themen auf humorvolle und übertriebene Weise darstellen. Die Inhalte zielen darauf ab, durch Übertreibung und Parodie aktuelle Missstände und Absurditäten aufzuzeigen und damit sowohl zum Lachen als auch zum Nachdenken anzuregen. Zudem ist das Titanic Magazin als eine der führenden Satirezeitschriften im deutschsprachigen Raum bekannt, was die satirische Absicht ihrer Beiträge für die Nutzer eindeutig macht."
    }
    for key, value in trustedSourcesDict.items():
        new_channel = Channel(channel_name=key, content=value, validity="Eher Vertrauenswürdig")
        db.session.add(new_channel)
    for key, value in untrustedSourcesDict.items():
        new_channel = Channel(channel_name=key, content=value, validity="Eher nicht Vertrauenswürdig")
        db.session.add(new_channel)
    for key, value in satireDict.items():
        new_channel = Channel(channel_name=key, content=value, validity="Satire")
        db.session.add(new_channel)




if __name__ == "__main__":
    #init_db()
    app.run(host="0.0.0.0",debug=True)