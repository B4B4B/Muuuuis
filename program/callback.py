
from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_PHOTO,
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" **مرحبآ عزيزي ↤「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」**\n
⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰
**⌯ انا بوت {BOT_NAME} استطيع تشغيل الموسيقي والفيديو في محادثتك الصوتية**

**⌯ لتعلم طريقة تشغيلي بمجموعتك اضغط علي » طريقة التفعيل !

**⌯ لمعرفة الاوامر اضغط علي  » الاوامر !
⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰ .
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𓄼الحساب المساعد𓄹", url=f"https://t.me/lddda"),
                ],
                [InlineKeyboardButton("𓄼طريقة التفعيل𓄹", callback_data="cbhowtouse")],
                [InlineKeyboardButton("𓄼الاوامــر𓄹", callback_data="cbcmds"),          
                [
                    InlineKeyboardButton("اضف البوت  لمجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" طريقة تفعيل البوت:-
 ⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰
 1 ↤ ضيف البوت إلى مجموعتك
 2 ↤ ارفع بوت ادمن 
 3 ↤ اكتب `تحديث` لتحديث بيانات المشرفين
 3 ↤ اكتب  `انضم` لدعوة حساب المساعد او ضيف الحساب  `@{ASSISTANT_NAME}`إلى مجموعتك 
 4 ↤ قبل استخدام امر تشغيل تاكد من الكول مفتوح
 5 ↤ لو كان اكو مشكلة في تشغيل اكتب `غادر`   من ثم  اكتب `انضم`    

 ⌯ عندك اي سؤال خلي بكلبك ما فارغلك
 ⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰

__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**⇦ قم بالضغط علي الزر الذي تريده لمعرفه الاوامر  !**

⌯ __مطور السورس @MOA_YAD __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𓄼اوامــر تشغيل𓄹", callback_data="cbadmin"),
                    InlineKeyboardButton("𓄹اوامر ثانية𓄹", callback_data="cbvamp"),
                ],[
                    InlineKeyboardButton("𓄼اوامــر تحميل والمطور𓄹", callback_data="cbsudo"),
                ],
                [
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰
⌯ | لتحميل اغاني أرسل ↞ ⊰ `تحميل + اسم اغنية` ⊱
⌯ | لتحميل فيديوهات ↞ ⊰ `تحميل_فيديو + اسم فيديو` ⊱
⌯ | لبحث عنه باليوتيوب  ↞ ⊰ `بحث` ⊱
⌯ | يجيبلك كلمات اي اغنية .  ↞ ⊰ `كلمات` ⊱
⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰
⌯ |  لإظهار حالة البوت أرسل ↞ ⊰ `بنك` ⊱
⌯ | لاظهار وقت تشغيل البوت أرسل ↞ ⊰ `بنك2` ⊱
⌯ | لإظهار معلومات البوت أرسل ↞ ⊰ `السورس ` ⊱
⌯ | لإظهار مطورين البوت أرسل ↞ ⊰ `المطور` ⊱
⌯ | لمسح جميع الملفات المستخدمه أرسل ↞ ⊰ `مسح` ⊱
⌯ | لتنظيف جميع الملفات المحمله أرسل ↞ ⊰ `تنظيف` ⊱
⌯ | لرؤيه معلومات السيرفر  البوت أرسل ↞ ⊰ `السيرفر` ⊱
⌯ | لتحديث البوت لاخر اصدار من السورس أرسل ↞ ⊰ `ترقيه` ⊱
⌯ | لاعادة تشغيل البوت أرسل ↞ ⊰ `ريستارت` ⊱
⌯ | لمغادره الحساب المساعد لجميع جروبات أرسل ↞ ⊰ `غادر الجميع` ⊱
⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰

__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""  ⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰
⌯ | لتشغيل صوتية في المكالمة أرسل ↞ ⊰ `تشغيل +اسم الأغنيةاو رابط` ⊱

⌯ | لتشغيل فيديو في المكالمة  ↞ ⊰ `فيديو +اسم الفديو او رابط` ⊱

⌯ | لتشغيل فيديو مباشر في المكالمة  ↞ ⊰ `فيديو_مباشر+رابط+جودة 360 - 480- 720 ` ⊱

⌯ | لأيقاف الاغنية  ↞ ⊰ `ايقاف`⊱   او   ⊰ `انهاء` ⊱

⌯ | لأيقاف الاغنية او الفيديو مؤقتآ  ↞ ⊰`موقت`⊱ او  ⊰ `وقف` ⊱

⌯ | لمتابعه تشغيل الاغنية ↞  ⊰ `متابعه` ⊱     او    ⊰ `كمل` ⊱

⌯ | لتخطي الاغنية  ↞ ⊰ `سكب`⊱ او ⊰ `تخطي` ⊱

⌯ | لعرض قائمه تشغيل  ↞  ⊰ `قائمه` ⊱

 ⌯ | لكتم البوت ↞  ⊰ `كتم ` ⊱ 

⌯ | الغاء الكتم البوت  ⊰ `الغاء الكتم` ⊱ 
⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰

__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰
⌯ | لتحميل اغاني أرسل ↞ ⊰ `تحميل + اسم اغنية` ⊱
⌯ | لتحميل فيديوهات ↞ ⊰ `تحميل_فيديو + اسم فيديو` ⊱
⌯ | لبحث عنه باليوتيوب  ↞ ⊰ `بحث` ⊱
⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰
⌯ |  لإظهار حالة البوت بينج  أرسل ↞ ⊰ `بنك ` ⊱
⌯ | لاظهار وقت تشغيل البوت أرسل ↞ ⊰ `بنك2` ⊱
⌯ | لإظهار معلومات البوت أرسل ↞ ⊰ `السورس ` ⊱
⌯ | لإظهار مطورين البوت أرسل ↞ ⊰ `المطور` ⊱
⌯ | لمسح جميع الملفات المستخدمه أرسل ↞ ⊰ `مسح` ⊱
⌯ | لتنظيف جميع الملفات المحمله أرسل ↞ ⊰ `تنضيف` ⊱
⌯ | لرؤيه معلومات السيرفر  البوت أرسل ↞ ⊰ `السيرفر` ⊱
⌯ | لتحديث البوت لاخر اصدار من السورس أرسل ↞ ⊰ `ترقيه` ⊱
⌯ | لاعادة تشغيل البوت أرسل ↞ ⊰ `ريستارت` ⊱
⌯ | لمغادره الحساب المساعد لجميع جروبات أرسل ↞ ⊰ `غادر الجميع` ⊱
⊱┉┉┉⊶𓄼•MUISC•𓄹⊷┉┉┉⊰

__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("⌯ اغلاق ⌯", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
