import os

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN não foi configurado. No Termux use: export DISCORD_TOKEN='SEU_TOKEN'"
    )
