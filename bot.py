import random

import discord
from discord.ext import commands
from config import TOKEN


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

resenha_mutado = False
ultima_resposta = None


# =========================
# RESPOSTAS
# =========================

RESPOSTAS = {
    "oi": [
        "eae KKKKK",
        "fala aí",
        "opa, tudo certo?",
        "eae mano",
        "salve",
        "fala, o que manda?",
    ],

    "como_esta": [
        "tô de boa KKKKK",
        "tranquilo por aqui",
        "tô suave, e tu?",
        "vivendo aí né",
        "tô bem, mano",
    ],

    "risada": [
        "KKKKKKKKKKKK",
        "mano KKKKKKK",
        "KKKKKKKK calma aí",
        "tá rindo do quê?",
        "KKKKKK eu não aguento",
    ],

    "obrigado": [
        "tmj",
        "é nóis",
        "de nada, pô",
        "tranquilo",
        "tmj KKKKK",
    ],

    "xingamento": [
        "KKKKKKKK olha a educação",
        "calma, animal",
        "ih, ficou nervoso?",
        "KKKKKKKK começou",
        "que isso, meu mano",
    ],

    "amor": [
        "ihhh, tá apaixonado KKKKK",
        "rapaz, essa história tá interessante",
        "eita, o amor bateu forte",
        "KKKKKK conta essa história direito",
        "quem é a vítima?",
    ],

    "triste": [
        "pô mano, fica tranquilo",
        "vai ficar tudo bem",
        "tô contigo",
        "respira aí e fica de boa",
        "dias ruins acontecem",
    ],

    "sono": [
        "vai dormir então KKKKK",
        "sono bateu forte hein",
        "dorme aí, criatura",
        "boa noite antecipada KKKKK",
    ],

    "comida": [
        "agora tu falou minha língua",
        "KKKKKKKK comida é coisa séria",
        "qual comida?",
        "me deu fome agora",
        "bora comer então",
    ],

    "roblox": [
        "Roblox é resenha demais KKKKK",
        "qual jogo do Roblox?",
        "vai jogar o quê?",
        "KKKKKK Roblox nunca acaba",
    ],

    "minecraft": [
        "Minecraft é clássico",
        "vai construir ou só morrer pros mobs? KKKKK",
        "sobrevivência ou criativo?",
        "Minecraft é bom demais",
    ],

    "jogar": [
        "bora KKKKK",
        "qual jogo?",
        "partiu",
        "eu topo",
        "chama aí",
    ],

    "pergunta": [
        "boa pergunta...",
        "sei lá KKKKK",
        "essa aí me pegou",
        "depende",
        "talvez",
        "não faço ideia, mano",
    ],

    "geral": [
        "KKKKKK olha quem apareceu.",
        "eae, criatura",
        "fala logo, o que foi?",
        "ih rapaz...",
        "que foi?",
        "tô ouvindo.",
        "manda a boa.",
        "lá vem merda",
        "fala, desgraça",
        "KKKKKK isso não pode ser sério",
        "mano...",
        "tá, continua.",
        "qual foi agora?",
        "fala aí.",
        "tô aqui, infelizmente.",
        "o que tu quer comigo?",
        "pode falar.",
        "tu não tem jeito.",
        "aí tu me quebra.",
    ]
}


def escolher_resposta(lista):
    global ultima_resposta

    opcoes = [
        resposta
        for resposta in lista
        if resposta != ultima_resposta
    ]

    if not opcoes:
        opcoes = lista

    resposta = random.choice(opcoes)
    ultima_resposta = resposta

    return resposta


# =========================
# IDENTIFICAR ASSUNTO
# =========================

def responder(texto):

    texto = texto.lower()

    if any(x in texto for x in [
        "oi", "olá", "ola", "eae", "eai", "opa", "salve"
    ]):
        return escolher_resposta(RESPOSTAS["oi"])

    if any(x in texto for x in [
        "tudo bem", "como você está", "como vc está",
        "como voce esta", "como vc ta", "como você tá"
    ]):
        return escolher_resposta(RESPOSTAS["como_esta"])

    if any(x in texto for x in [
        "kkkk", "haha", "hahaha", "rsrs"
    ]):
        return escolher_resposta(RESPOSTAS["risada"])

    if any(x in texto for x in [
        "obrigado", "obrigada", "valeu", "vlw", "tmj"
    ]):
        return escolher_resposta(RESPOSTAS["obrigado"])

    if any(x in texto for x in [
        "idiota", "burro", "burra", "otario", "otário",
        "fdp", "desgraçado", "desgracado", "porra", "caralho"
    ]):
        return escolher_resposta(RESPOSTAS["xingamento"])

    if any(x in texto for x in [
        "amor", "apaixonado", "apaixonada",
        "namorada", "namorado", "crush"
    ]):
        return escolher_resposta(RESPOSTAS["amor"])

    if any(x in texto for x in [
        "triste", "chorando", "chorei", "mal",
        "desanimado", "desanimada"
    ]):
        return escolher_resposta(RESPOSTAS["triste"])

    if any(x in texto for x in [
        "sono", "dormir", "dormindo", "cansado", "cansada"
    ]):
        return escolher_resposta(RESPOSTAS["sono"])

    if any(x in texto for x in [
        "comida", "comer", "fome", "pizza", "hamburguer",
        "hambúrguer", "lanche"
    ]):
        return escolher_resposta(RESPOSTAS["comida"])

    if "roblox" in texto:
        return escolher_resposta(RESPOSTAS["roblox"])

    if "minecraft" in texto:
        return escolher_resposta(RESPOSTAS["minecraft"])

    if any(x in texto for x in [
        "jogar", "jogo", "game", "jogando"
    ]):
        return escolher_resposta(RESPOSTAS["jogar"])

    if "?" in texto:
        return escolher_resposta(RESPOSTAS["pergunta"])

    return escolher_resposta(RESPOSTAS["geral"])


# =========================
# BOT ONLINE
# =========================

@bot.event
async def on_ready():

    print(f"🤖 Resenha online como {bot.user}")
    print(f"🌐 Servidores: {len(bot.guilds)}")

    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} comandos slash sincronizados.")
    except Exception as e:
        print(f"❌ Erro ao sincronizar: {e}")


# =========================
# CONVERSA
# =========================

@bot.event
async def on_message(message):

    global resenha_mutado

    if message.author.bot:
        return

    await bot.process_commands(message)

    if bot.user not in message.mentions:
        return

    if resenha_mutado:
        return

    texto = message.content.lower()

    texto = texto.replace(
        f"<@{bot.user.id}>",
        ""
    )

    texto = texto.replace(
        f"<@!{bot.user.id}>",
        ""
    )

    texto = texto.strip()

    if not texto:
        await message.reply(
            escolher_resposta([
                "KKKKKK tu me chamou sem falar nada?",
                "que foi?",
                "fala aí.",
                "me chamou pra ficar olhando?",
                "KKKKKKKKKK e eu faço o quê?",
            ])
        )
        return

    await message.reply(responder(texto))


# =========================
# MUTE
# =========================

@bot.tree.command(
    name="muteresenha",
    description="Desliga as respostas do Resenha"
)
async def muteresenha(interaction: discord.Interaction):

    global resenha_mutado

    resenha_mutado = True

    await interaction.response.send_message(
        "🔇 Resenha mutado!"
    )


# =========================
# UNMUTE
# =========================

@bot.tree.command(
    name="unmuteresenha",
    description="Liga novamente as respostas do Resenha"
)
async def unmuteresenha(interaction: discord.Interaction):

    global resenha_mutado

    resenha_mutado = False

    await interaction.response.send_message(
        "🔊 Resenha desmutado!"
    )


# =========================
# OI
# =========================

@bot.tree.command(
    name="oi",
    description="O Resenha manda um oi"
)
async def oi(interaction: discord.Interaction):

    await interaction.response.send_message(
        f"Fala, {interaction.user.mention}!"
    )


# =========================
# PING
# =========================

@bot.tree.command(
    name="ping",
    description="Mostra a latência do bot"
)
async def ping(interaction: discord.Interaction):

    ms = round(bot.latency * 1000)

    await interaction.response.send_message(
        f"🏓 Pong! `{ms}ms`"
    )


# =========================
# DADO
# =========================

@bot.tree.command(
    name="dado",
    description="Rola um dado"
)
async def dado(interaction: discord.Interaction):

    numero = random.randint(1, 6)

    await interaction.response.send_message(
        f"🎲 Você tirou **{numero}**!"
    )


# =========================
# CARA OU COROA
# =========================

@bot.tree.command(
    name="caraoucoroa",
    description="Joga cara ou coroa"
)
async def caraoucoroa(interaction: discord.Interaction):

    resultado = random.choice([
        "🪙 Cara!",
        "🪙 Coroa!"
    ])

    await interaction.response.send_message(resultado)


# =========================
# SORTE
# =========================

@bot.tree.command(
    name="sorte",
    description="Descobre sua sorte"
)
async def sorte(interaction: discord.Interaction):

    porcentagem = random.randint(0, 100)

    await interaction.response.send_message(
        f"🍀 Sua sorte hoje é de **{porcentagem}%**!"
    )


# =========================
# 8BALL
# =========================

@bot.tree.command(
    name="8ball",
    description="Faça uma pergunta para a bola 8"
)
async def oito_ball(interaction: discord.Interaction):

    respostas = [
        "🎱 Com certeza.",
        "🎱 Provavelmente.",
        "🎱 Sim.",
        "🎱 Não.",
        "🎱 Acho que não.",
        "🎱 Melhor não perguntar.",
        "🎱 O futuro dirá.",
    ]

    await interaction.response.send_message(
        random.choice(respostas)
    )


# =========================
# SHIP
# =========================

@bot.tree.command(
    name="ship",
    description="Calcula uma porcentagem de combinação"
)
async def ship(interaction: discord.Interaction):

    porcentagem = random.randint(0, 100)

    await interaction.response.send_message(
        f"💘 Combinação: **{porcentagem}%**"
    )


# =========================
# RESENHA
# =========================

@bot.tree.command(
    name="resenha",
    description="Fala uma frase aleatória"
)
async def resenha(interaction: discord.Interaction):

    await interaction.response.send_message(
        escolher_resposta(RESPOSTAS["geral"])
    )


# =========================
# INICIAR
# =========================

bot.run(TOKEN)
