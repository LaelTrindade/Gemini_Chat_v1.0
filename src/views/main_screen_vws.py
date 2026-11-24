import socket
import threading
from PIL import Image, ImageTk
import customtkinter as ctk
from src.utils.config import ASSETS_DIR
from src.services.agent_svc import chamar_agente, MODEL_NAME


def load_app():

    """ todo 
        > Inicializando o app e centralizando ao meio da tela;
        > Definindo tema padrão como dark (escuro) e botões azuis."""

    app = ctk.CTk()
    app.title('Gemini AI - New Chat')

    window_width = 720
    window_height = 540

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')
    
    app.geometry(f'{window_width}x{window_height}+{x}+{y}')
    app.configure(fg_color = '#1E293B')

    icon_img = ImageTk.PhotoImage(Image.open(ASSETS_DIR/'icon_logo.png'))
    app.iconphoto(True, icon_img)

    main_frame = ctk.CTkFrame(
        master = app,
        border_width = 1,
        corner_radius = 20,
        fg_color = '#0F172A',
        border_color = '#334155'
    )

    app.grid_columnconfigure(0, weight = 1)
    app.grid_rowconfigure(0, weight = 1)

    main_frame.grid(row = 0, column = 0, sticky = 'nsew', padx = 5, pady = 5)

    top_frame = ctk.CTkFrame(
        master = main_frame,
        height = 50,
        fg_color = 'transparent'
    )

    main_frame.grid_columnconfigure(0, weight = 1)

    top_frame.grid(row = 0, column = 0, sticky = 'ew', padx = 2, pady = (12, 6))
    top_frame.pack_propagate(False)

    label_model = ctk.CTkLabel(
        master = top_frame,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        text_color = '#FFFFFF',
        fg_color = 'transparent',
        text = f'   {MODEL_NAME}',
        font = ('Inter', 18, 'bold'),
        image = ctk.CTkImage(
            dark_image = Image.open(ASSETS_DIR/'gemini_icon.png'),
            light_image = Image.open(ASSETS_DIR/'gemini_icon.png'),
            size = ((32, 32))
        )
    )

    label_model.pack(side = 'left', padx = (20, 0), pady = 0)

    online_icon = ctk.CTkImage(
        dark_image = Image.open(ASSETS_DIR/'green_circle_icon.png'),
        light_image = Image.open(ASSETS_DIR/'green_circle_icon.png'),
        size = ((14, 14))
    )

    offline_icon = ctk.CTkImage(
        dark_image = Image.open(ASSETS_DIR/'red_circle_icon.png'),
        light_image = Image.open(ASSETS_DIR/'red_circle_icon.png'),
        size = ((14, 14))
    )


    def verificar_conexao():
        def testar():
            try:
                socket.create_connection(('8.8.8.8', 53), timeout = 3).close()
                online = True
            except OSError:
                online = False

            app.after(0, lambda: atualizar_status(online))

        threading.Thread(target = testar, daemon = True).start()


    def atualizar_status(online):
        label_status.configure(image = online_icon if online else offline_icon)
        label_status.configure(text_color = '#22C55E' if online else '#EF4444')
        label_status.configure(text = ' Online' if online else ' Offline')
        
        app.after(5000, verificar_conexao)


    label_status = ctk.CTkLabel(
        master = top_frame,
        width = 0,
        height = 0,
        anchor = 'w',
        compound = 'left',
        text_color = '#22C55E',
        fg_color = 'transparent',
        text = ' Online',
        font = ('Inter', 16),
        image = ctk.CTkImage(
            dark_image = Image.open(ASSETS_DIR/'green_circle_icon.png'),
            light_image = Image.open(ASSETS_DIR/'green_circle_icon.png'),
            size = ((14, 14))
        )
    )

    label_status.pack(side = 'right', padx = (0, 25), pady = 0)

    frame_line = ctk.CTkFrame(
        master = main_frame,
        height = 2,
        corner_radius = 0,
        fg_color = '#334155'
    )

    frame_line.grid(row = 1, column = 0, sticky = 'ew', columnspan = 2)

    conteudo_frame = ctk.CTkScrollableFrame(
        master = main_frame,
        fg_color = 'transparent',
        scrollbar_button_color = '#334155',
        scrollbar_button_hover_color = '#475569'
    )

    conteudo_frame.grid(row = 2, column = 0, sticky = 'nsew', padx = 5, pady = 5)

    bottom_frame = ctk.CTkFrame(
        master = main_frame,
        height = 55,
        border_width = 1,
        corner_radius = 10,
        fg_color = '#334155',
        bg_color = '#1E293B',
        border_color = '#475569'
    )

    main_frame.grid_rowconfigure(2, weight = 1)

    bottom_frame.grid(row = 3, column = 0, sticky = 'sew', padx = 0, pady = 0)

    entry = ctk.CTkEntry(
        master = bottom_frame,
        corner_radius = 5,
        border_width = 0,
        font = ('Inter', 14),
        fg_color = '#0F172A',
        text_color = '#FFFFFF'
    )

    entry.pack(side = 'left', fill = 'x', expand = True, padx = 5, pady = 5)

    button = ctk.CTkButton(
        master = bottom_frame,
        width = 30,
        height = 30,
        text = '',
        corner_radius = 10,
        cursor = 'hand2',
        fg_color = '#285A85',
        hover_color = '#214B70',
        image = ctk.CTkImage(
            dark_image = Image.open(ASSETS_DIR/'arrow_icon.png'),
            light_image = Image.open(ASSETS_DIR/'arrow_icon.png'),
            size = ((21, 21))
        )
    )

    button.pack(side = 'right', padx = (2, 5), pady = 5)

    def adicionar_mensagem(texto, autor):

        usuario = autor == 'user'

        balloon = ctk.CTkFrame(
            master = conteudo_frame,
            corner_radius = 12,
            fg_color = '#285A85' if usuario else '#334155'
        )

        balloon.pack(anchor = 'e' if usuario else 'w', padx = 10, pady = 4)

        message = ctk.CTkLabel(
            master = balloon,
            text = texto,
            wraplength = 420,
            justify = 'left',
            text_color = '#FFFFFF',
            font = ('Inter', 14)
        )

        message.pack(padx = 12, pady = 8)

        app.after(50, lambda: conteudo_frame._parent_canvas.yview_moveto(1.0))


    def enviar_mensagem(event = None):
        texto = entry.get().strip()

        if not texto or button.cget('state') == 'disabled':
            return

        entry.delete(0, 'end')
        adicionar_mensagem(texto, 'user')
        button.configure(state = 'disabled')

        def processar():
            try:
                resposta = chamar_agente(texto)
            except Exception as erro:
                resposta = f'Erro: {erro}'

            app.after(0, lambda: receber_resposta(str(resposta)))

        threading.Thread(target = processar, daemon = True).start()


    def receber_resposta(resposta):
        adicionar_mensagem(resposta, 'ia')
        button.configure(state = 'normal')


    button.configure(command = enviar_mensagem)
    entry.bind('<Return>', enviar_mensagem)

    verificar_conexao()
    

    app.mainloop()