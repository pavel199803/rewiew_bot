from aiogram import Router, Bot, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()


class Form(StatesGroup):
    review_more_photo = State()
    review_add_photo = State()
    review_grade = State()
    review_name = State()
    review_text = State()
    review_end = State()
    review_photo = State()


m = []

kb_anon = [
    [
        types.KeyboardButton(text="Анонимно🙈"),
        types.KeyboardButton(text="Назвать имя👋🏼")
    ],
]
r_keyboard_anon = types.ReplyKeyboardMarkup(
    keyboard=kb_anon,
    resize_keyboard=True,
    one_time_keyboard=True
)

inline_photo = InlineKeyboardButton(
    text="Прикрепить фото💙",
    callback_data="inline_photo_pressed",
)

inline_onwards = InlineKeyboardButton(
    text="Далее👉🏼",
    callback_data="inline_onwards_pressed",
)

inline_grade_1 = InlineKeyboardButton(
    text="1️⃣",
    callback_data="inline_grade_1_pressed",
)
inline_grade_2 = InlineKeyboardButton(
    text="2️⃣",
    callback_data="inline_grade_2_pressed"
)
inline_grade_3 = InlineKeyboardButton(
    text="3️⃣",
    callback_data="inline_grade_3_pressed"

)
inline_grade_4 = InlineKeyboardButton(
    text="4️⃣",
    callback_data="inline_grade_4_pressed"
)
inline_grade_5 = InlineKeyboardButton(
    text="5️⃣",
    callback_data="inline_grade_5_pressed"
)
inline_tg = InlineKeyboardButton(
    text="Наш Канал",
    url='https://t.me/marketsletatspb'
)
inline_chat_bot = InlineKeyboardButton(
    text="ТурАссистент",
    url='https://t.me/assistant_market_sletat_bot'
)
inline_more = InlineKeyboardButton(
    text="Оставить отзыв",
    callback_data="inline_more_pressed"
)
inline_tours = InlineKeyboardButton(
    text="Туры дня || Маркет Слетать🛫",
    url='https://t.me/marketsletat_tours'
)
i_keyboard = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          inline_grade_1,
                                          inline_grade_2,
                                          inline_grade_3,
                                          inline_grade_4,
                                          inline_grade_5
                                      ]
                                  ])
i_keyboard_photo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            inline_photo,
            inline_onwards
        ]
    ]

)
i_keyboard_end = InlineKeyboardMarkup(
    inline_keyboard=[
        [inline_more],
        [inline_tg, inline_chat_bot],
        [inline_tours]
    ]
)


@router.message(CommandStart())
async def command_start(message: types.Message, state: FSMContext):
    await state.update_data(username=message.from_user.username)
    await message.answer(
        "Здравствуйте!) Вы перешли в бот <b>«Маркет Слетать»,</b> который помогает собирать <u>обратную связь от "
        "туристов,</u>"
        "чтобы мы становились лучше💙\n\n"
        "Подскажите, вы желаете оставить анонимный отзыв или хотите назвать свое имя?\n\n",
        reply_markup=r_keyboard_anon
    )
    await state.set_state(Form.review_name)


@router.callback_query(F.data == "inline_more_pressed")
async def review_more(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(username=callback.from_user.username)
    await callback.answer("🛫")
    await callback.message.answer(
        "Здравствуйте!) Вы перешли в бот <b>«Маркет Слетать»,</b> который помогает собирать <u>обратную связь от "
        "туристов,</u>"
        "чтобы мы становились лучше💙\n\n"
        "Подскажите, вы желаете оставить анонимный отзыв или хотите назвать свое имя?\n\n",
        reply_markup=r_keyboard_anon
    )
    await state.set_state(Form.review_name)


@router.message(Form.review_name)
async def review_name(message: types.Message, state: FSMContext):
    await state.update_data(anon=message.text)
    data = await state.get_data()
    if data['anon'] == "Анонимно🙈":
        await message.answer("Оцените, пожалуйста, работу вашего менеджера от 1 до 5🙏🏼", reply_markup=i_keyboard)
    elif data['anon'] == "Назвать имя👋🏼":
        await message.answer("Хорошо!) Представьтесь, пожалуйста☺️")
        await state.set_state(Form.review_grade)
    else:
        await message.answer("выберете варианат")


@router.message(Form.review_grade)
async def review_photo(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await message.answer(
        f"{data['name']}, оцените, пожалуйста, работу вашего менеджера от 1 до 5🙏🏼",
        reply_markup=i_keyboard
    )


@router.callback_query(F.data == "inline_grade_1_pressed")
async def inline_grade_1(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("🛫")
    await state.update_data(grade=1)
    data = await state.get_data()
    await callback.message.answer(
        "Благодарим за вашу оценку💙 Нам очень важно понять, что конкретно вам не понравилось😔\n\n"
        "Не могли бы вы описать, что вызвало у вас такие эмоции? Что в работе менеджера вас не устроило? Ваш отзыв "
        "позволит нам исправить недочеты в работе!"
    )
    await state.set_state(Form.review_photo)


@router.callback_query(F.data == "inline_grade_2_pressed")
async def inline_grade_2(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("🛫")
    await state.update_data(grade=2)
    data = await state.get_data()
    await callback.message.answer(
        "Благодарим за вашу оценку💙 Нам очень важно понять, что конкретно вам не понравилось😔\n\n"
        "Не могли бы вы описать, что вызвало у вас такие эмоции? Что в работе менеджера вас не устроило? Ваш отзыв "
        "позволит нам исправить недочеты в работе!"
    )
    await state.set_state(Form.review_photo)


@router.callback_query(F.data == "inline_grade_3_pressed")
async def inline_grade_3(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("🛫")
    await state.update_data(grade=3)
    data = await state.get_data()
    await callback.message.answer(
        "Благодарим за вашу оценку💙 Нам очень важно понять, что конкретно вам не понравилось😔\n\n"
        "Не могли бы вы описать, что вызвало у вас такие эмоции? Что в работе менеджера вас не устроило? Ваш отзыв "
        "позволит нам исправить недочеты в работе!"
    )
    await state.set_state(Form.review_photo)


@router.callback_query(F.data == "inline_grade_4_pressed")
async def inline_grade_4(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("🛫")
    await state.update_data(grade=4)
    data = await state.get_data()
    await callback.message.answer(
        "Благодарим за вашу оценку, это очень важно для нас!💙 Ниже мы оставили пару вопросов, чтобы вы смогли "
        "оставить более подробный отзыв🙌🏼\n\n"
        "• Не могли бы вы описать, почему выбрали наше агентство?\n"
        "• Что конкретно понравилось вам при работе с менеджером?\n"
        "• Довольны ли вы своим отдыхом?\n"
        "• Будете ли обращаться к нам снова?\n"

    )
    await state.set_state(Form.review_photo)


@router.callback_query(F.data == "inline_grade_5_pressed")
async def inline_grade_5(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("🛫")
    await state.update_data(grade=5)
    data = await state.get_data()
    await callback.message.answer(
        "Благодарим за вашу оценку, это очень важно для нас!💙 Ниже мы оставили пару вопросов, чтобы вы смогли "
        "оставить более подробный отзыв🙌🏼\n\n"
        "• Не могли бы вы описать, почему выбрали наше агентство?\n"
        "• Что конкретно понравилось вам при работе с менеджером?\n"
        "• Довольны ли вы своим отдыхом?\n"
        "• Будете ли обращаться к нам снова?\n"

    )
    await state.set_state(Form.review_photo)


@router.message(Form.review_photo)
async def review_photo(message: types.Message, state: FSMContext):
    await state.update_data(review=message.text)
    await message.answer("Приложите фотографии из отпуска, если хотите🫶🏼", reply_markup=i_keyboard_photo)


@router.callback_query(F.data == "inline_photo_pressed")
async def review_photo_add(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("🛫")
    await callback.message.answer("Отлично! Подсказка: отправьте одновременно не более 10 фотографий")
    await state.set_state(Form.review_more_photo)


@router.message(Form.review_more_photo)
async def review_more_photo(message: types.Message, bot: Bot):
    global m
    date = message.date
    if [message.chat.id, date] not in m:
        m.append([message.chat.id, date])  # Добавляем в список id пользователя и дату отправки
        await message.answer("Хотите добавить еще фото?", reply_markup=i_keyboard_photo)
    await bot.forward_message(-1002005451511, message.from_user.id, message.message_id)


@router.callback_query(F.data == "inline_onwards_pressed")
async def review_onwards(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    await callback.answer("🛫")
    data = await state.get_data()
    if data['grade'] <= 4:
        if data['anon'] == "Назвать имя👋🏼":
            await callback.message.answer(
                f"{data['name']}! Спасибо за ваши слова. "
                f"Мы обязательно передадим их в отдел качества и вашему персональному менеджеру☺️\n\n"
                f"Будем рады увидеться в новых путешествиях🛫",
                reply_markup=i_keyboard_end
            )
        else:
            await callback.message.answer(
                f"Спасибо за ваши слова. "
                f"Мы обязательно передадим их в отдел качества и вашему персональному менеджеру☺️\n\n"
                f"Будем рады увидеться в новых путешествиях🛫",
                reply_markup=i_keyboard_end
            )
    else:
        if data['anon'] == "Назвать имя👋🏼":
            await callback.message.answer(
                f"{data['name']}! Спасибо, что поделились. Мы обязательно передадим ваш отзыв в отдел качества!)"
                f"Будем рады увидеться в новых путешествиях🛫",
                reply_markup=i_keyboard_end
            )
        else:
            await callback.message.answer(
                "Спасибо, что поделились. Мы обязательно передадим ваш отзыв в отдел качества!)"
                "Будем рады увидеться в новых путешествиях🛫",
                reply_markup=i_keyboard_end
            )
    if data['anon'] == "Назвать имя👋🏼":
        await bot.send_message(-1002005451511,
                               f"Имя: {data['name']}\n"
                               f"ТГ username: @{data['username']}\n"
                               f"Оценка: {data['grade']}\n"
                               f"Отзыв:\n {data['review']}"
                               )
    else:
        await bot.send_message(-1002005451511,
                               f"Анонимный отзыв.\n"
                               f"ТГ username: @{data['username']}\n"
                               f"Оценка: {data['grade']}\n"
                               f"Отзыв:\n {data['review']}"
                               )
