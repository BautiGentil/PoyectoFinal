import random, os
import discord
from model import get_class

# La variable intents almacena los privilegios del bot

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola! soy {bot.user}, el bot de este server :D')


 
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def consejos(ctx):
    await ctx.send(f'-consejos para evitar la contaminacion: ')
    T=['Arrojar la basura donde corresponde','Colaborar con centros comunitarios de reciclaje','Disminuir al máximo el uso del automóvil y la motocicleta; preferir caminar, usar bicicleta o el transporte público.','Reduce el consumo de plásticos',"Disminuye el uso del agua y de la energía eléctrica.","Evita quemar basura, hojas y otros objetos, así como hacer fogatas en bosques o en plena ciudad"]
    tip = random.choice(T)
    await ctx.send(tip)

@bot.command()
async def que_es(ctx):
    await ctx.send(f'¿Que es la contaminacion?')
    await ctx.send('La contaminación supone la introducción de sustancias u otros elementos físicos en un medio que lo hacen inseguro y no apto para ser utilizado. El medio puede ser un ecosistema, un medio físico o un ser vivo y la sustancia contaminante puede ser una sustancia química, el sonido, el calor, la luz o la radioactividad.')

@bot.command()
async def tipos(ctx):
    await ctx.send(f'tipos de contaminacion: ')
    T=['Contaminación del aire: Supone la liberación de sustancias en la atmósfera que alteran su composición y hacen que sea nociva para el hombre, los animales o las plantas. Algunas de las sustancias más contaminantes son: el monóxido de carbono, el dióxido de azufre o el óxido de nitrógeno.',"Contaminación del agua: Se produce cuando se liberan contaminantes en el agua que transportan los ríos, en el mar o en aguas subterráneas. Un ejemplo de esto son los plásticos que terminan en el mar o los derrames de petróleo que se han producido en mares y océanos.","Contaminación de la tierra: Ocurre cuando determinados productos químicos se filtran sobre o bajo tierra. Suele suceder con el petróleo y con metales pesados. Otros químicos que también contaminan la tierra son los herbicidas y plaguicidas que se utilizan en la agricultura.","Contaminación térmica: Se produce cuando aumenta la temperatura del agua, por ejemplo, y produce efectos negativos sobre los seres vivos.","Contaminación acústica: Cualquiera que haya vivido en una gran ciudad ha sufrido ruido de: aviones, helicópteros, ambulancias, coches, grandes aglomeraciones de personas, etc..."]
    tip = random.choice(T)
    await ctx.send(tip)

@bot.command()
async def manualidades(ctx):
    await ctx.send(f'Ideas de manualidades resiclables: ')
    T=['https://youtu.be/D_u6mNlHprE',"https://youtu.be/d_U4Vw3T4r4","https://youtu.be/Cx2vm31y0IA"]
    tip = random.choice(T)
    await ctx.send(tip)

@bot.command()
async def mems(ctx):

    image = random.choice(os.listdir("images"))

    with open(f'images/{image}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(f"Imagen guardada en ./{file_url}")
            try: 
                clase = get_class(model_path = "keras_model.h5", labels_path = "labels.txt", image_path = f"./{file_name}"  )
                if clase[0] == "Palomas":
                    await ctx.send("Es posiblemente una paloma paloma, pueden comer todo tipo de granos como trigo")
                elif clase[0] == "Gorriones":
                    await ctx.send("Es posiblemente un gorrión, pueden comer todo tipo de granos como arroz")
            
            except:
                await ctx.send("Ha ocurrido un error, intentalo de nuevo please :C")
    else:
        await ctx.send("No subiste una imagen :(")
        

bot.run("Token")
