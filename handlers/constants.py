user_roles = {"regular_user": "regular_user", "ask_help": "ask_help", "offer_help": "offer_help"}
phone_reg = r"^\+380([0-9]{9})$"
welcome_text = (
    "Друзі, вітаємо! 🇺🇦\n\n"
    "Мета цього чат-боту — допомогти організувати безпечну, "
    "надійну роботу волонтерів та упорядкувати систему запитів.\n\n"
    "У роботі є такі розділи:\n"
    "🆘 Мені потрібна допомога\n"
    "🙏 Я хочу надати допомогу\n💸 Підтримати фінансово\n"
    "📣 Розповісти іншим\n\n"
    "Як працює чат-бот?\n"
    "✅ Усі волонтери проходять перевірку на безпеку.\n"
    "✅ Волонтер отримує конкретне завдання та відмічає статус виконання, "
    "таким чином ми оптимізуємо ресурси, ефективно та адресно надаємо допомогу.\n"
    "✅ Чат-бот підтримує велика команда волонтерів-координаторів, "
    "які надають підтримку на етапі оформлення заявки та особисто відповідають за її виконання.\n\n"
    "Долучайтесь!  Слава Україні! 💙💛"
)

help_text = (
    "Оберіть потрібний вам розділ:\n\n"
    "🆘 Мені потрібна допомога\n\n"
    "🔸 вкажіть населений пункт, де потрібна допомога;\n"
    "🔸 оберіть в чому необхідна допомога (розділ);\n"
    "🔸 потім чітко, коротко і по суті опишіть, що вам потрібно;\n"
    "💌 Ваш запит буде надіслано всім зареєстрованим волонтерам регіону.\n"
    "💌 Ви отримаєте контакт людини, яка погодилась допомогти і зможете з нею зв’язатись.\n"
    "💌 За вашою заявкою прикріплюється координатор який несе особисту відповідальність за виконання вашої заявки.\n\n"
    "🙏 Я хочу надати допомогу\n\n🔹 оберіть розділ (як саме ви можете допомогти);\n"
    "🔹 вкажіть населений пункт, де ви можете допомогти;\n\n"
    "💌 Наші координатори будуть надсилати вам конкретні задачі на допомогу;\n"
    "💌 Ми піклуємось про те, щоб завдання були посильними та зручними  для вас (в місці вашого проживання);\n"
    "💌 По можливості, ми забезпечимо вас чіткими інструкціями де взяти ресурси та кошти на їх закупівлю.\n\n"
    "💸 Підтримати фінансово\n\n"
    "Якщо ви не можете допомогти фізично- можете перерахувати кошти на підтримку проекту. "
    "За вашим запитом, ми надамо детальну звітність коли "
    "і куди була витрачена кожна гривня фінансової допомоги."
)
donate_text = (
    '🙏 Мета чат-боту "Армія Волонтерів" — допомогти організувати безпечну,'
    " надійну допомогу всім, хто її потребує.\n\n"
    "✅ Ми приймаємо фінансову допомогу для придбання ліків,"
    " їжі та інших необхідних гуманітарних продуктів\n\n"
    "Ми ведемо звітнісь щодо надходження та витрат кожної копійки. Дивись тут volonter.net.ua\n\n"
    "Реквізити для оплати:\n"
    "ФОП Степанов Дмитро Миколайович\n"
    "ЕГРПОУ 3338915437\n"
    "1️⃣  `UA573133990000026005000207113`\n"
    "АО КБ «Приватбанк»\n"
    "Карты:\n"
    "Ключ до рахунку – стандартно для прийому та платежів\n"
    "`4246001030132488`\n\n"
    "ФОП Стапанов Дмитро Миколайович\n"
    "2️⃣  `UA083220010000026005310083364`\n"
    "АТ «Універсал банк»\n"
    "Карта Монобанк\n"
    "`4035200040997105`"
)

share_text = (
    "💙💛Друзі, ми прагнемо надати безпечну допомогу всім, хто її потребує, "
    'тому  просимо  вас поширити інформацію про чат-бот "Армія Волонтерів".\n\n'
    '✅Для цього, натисніть кнопку "Поділитись" та '
    "відмітьте друзів, яким надійде посилання: t.me/volonterarmy_bot"
)

admin_contact_text = "💬У разі виникнення питань, зв'язок з адміністрацією можливий за номером: `0674971125`"

__all__ = ["user_roles", "phone_reg", "welcome_text", "help_text", "donate_text", "share_text", "admin_contact_text"]
