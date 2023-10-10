from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")


article_text = """
    С 1 октября российский Центробанк начал по-новому рассекречивать мошенников, напомнил резидент Экспертного клуба ЦСР Глеб Белавин. Теперь банки начали передавать регулятору данные о переводах, которые кажутся сомнительными.

До этого ЦБ получал только сведения о конечном получателе похищенных средств. Теперь банки будут раскрывать информацию о подозрительных транзакциях по 50 признакам. Среди прочего, речь идет о большем количестве данных о переводах, сделанных без согласия владельца счета. Как говорил экономический обозреватель Вячеслав Абрамов, нововведение может принести некоторые дополнительные неудобства для бизнеса, но серьезных ухудшений не будет.

Ранее депутат Госдумы Денис Кравченко в разговоре с «Лентой.ру» заявил, что возможности мошенников уже существенно ограничены, что в значительной степени повышает уровень защиты граждан. Тем не менее работа по совершенствованию безопасности персональных данных россиян продолжается.
"""

candidate_labels = ["спорт", "политика", "экономика", "здоровье", "наука"]
output = classifier(article_text, candidate_labels, multi_label=False)
print(output)
