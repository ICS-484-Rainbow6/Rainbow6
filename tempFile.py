html.H1("Win Delta Per Operator VS Presence", style={'text-align': 'center'}),
    html.Div([
        html.H3("Platform:"),
            dcc.Dropdown(id="platform_select",
                         options=[
                             {"label": "All", "value": "None"},
                             {"label": "PC", "value": "PC"},
                             {"label": "PS4", "value": "PS4"},
                             {"label": "XONE", "value": "XONE"}],
                         multi=False,
                         value="None",
                         style={'width': '49%', 'display': 'inline-block'}
                         ),

        html.H3("Rank:"),
        dcc.Dropdown(id="rank_select",
                     options=[
                         {"label": "All", "value": "None"},
                         {"label": "Unranked", "value": "Unranked"},
                         {"label": "Copper", "value": "Copper"},
                         {"label": "Bronze", "value": "Bronze"},
                         {"label": "Silver", "value": "Silver"},
                         {"label": "Gold", "value": "Gold"},
                         {"label": "Platinum", "value": "Platinum"},
                         {"label": "Diamond", "value": "Diamond"}],
                     multi=False,
                     value="None",
                     style={'width': '49%', 'display': 'inline-block'}
                     ),

                html.H3("Map:"),
                dcc.Dropdown(id="map_select",
                             options=[
                                 {"label": "All", "value": "None"},
                                 {"label": "BANK", "value": "BANK"},
                                 {"label": "BARTLETT U.", "value": "BARTLETT U."},
                                 {"label": "BORDER", "value": "BORDER"},
                                 {"label": "CHALET", "value": "CHALET"},
                                 {"label": "CLUB HOUSE", "value": "CLUB HOUSE"},
                                 {"label": "COASTLINE", "value": "COASTLINE"},
                                 {"label": "CONSULATE", "value": "CONSULATE"},
                                 {"label": "FAVELAS", "value": "FAVELAS"},
                                 {"label": "HEREFORD BASE", "value": "HEREFORD BASE"},
                                 {"label": "HOUSE", "value": "HOUSE"},
                                 {"label": "KAFE DOSTOYEVSKY", "value": "KAFE DOSTOYEVSKY"},
                                 {"label": "KANAL", "value": "KANAL"},
                                 {"label": "OREGON", "value": "OREGON"},
                                 {"label": "PLANE", "value": "PLANE"},
                                 {"label": "SKYSCRAPER", "value": "SKYSCRAPER"},
                                 {"label": "YACHT", "value": "YACHT"}],
                             multi=False,
                             value="None",
                             style={'width': '49%', 'display': 'inline-block'}
                             ),

            html.H3("Operator:"),

            dcc.Dropdown(id="operator_select",
                         options=[
                             {"label": "BOPE-CAPITAO", "value": "BOPE-CAPITAO"},
                             {"label": "BOPE-CAVEIRA", "value": "BOPE-CAVEIRA"},
                             {"label": "G.E.O.-JACKAL", "value": "G.E.O.-JACKAL"},
                             {"label": "G.E.O.-MIRA", "value": "G.E.O.-MIRA"},
                             {"label": "GIGN-DOC", "value": "GIGN-DOC"},
                             {"label": "GIGN-MONTAGNE", "value": "GIGN-MONTAGNE"},
                             {"label": "GIGN-ROOK", "value": "GIGN-ROOK"},
                             {"label": "GIGN-TWITCH", "value": "GIGN-TWITCH"},
                             {"label": "GSG9-BANDIT", "value": "GSG9-BANDIT"},
                             {"label": "GSG9-BLITZ", "value": "GSG9-BLITZ"},
                             {"label": "GSG9-IQ", "value": "GSG9-IQ"},
                             {"label": "GSG9-JAGER", "value": "GSG9-JAGER"},
                             {"label": "JTF2-BUCK", "value": "JTF2-BUCK"},
                             {"label": "JTF2-FROST", "value": "JTF2-FROST"},
                             {"label": "NAVYSEAL-BLACKBEARD", "value": "NAVYSEAL-BLACKBEARD"},
                             {"label": "NAVYSEAL-VALKYRIE", "value": "NAVYSEAL-VALKYRIE"},
                             {"label": "SAS-MUTE", "value": "SAS-MUTE"},
                             {"label": "SAS-SLEDGE", "value": "SAS-SLEDGE"},
                             {"label": "SAS-SMOKE", "value": "SAS-SMOKE"},
                             {"label": "SAS-THATCHER", "value": "SAS-THATCHER"},
                             {"label": "SAT-ECHO", "value": "SAT-ECHO"},
                             {"label": "SAT-HIBANA", "value": "SAT-HIBANA"},
                             {"label": "SPETSNAZ-FUZE", "value": "SPETSNAZ-FUZE"},
                             {"label": "SPETSNAZ-GLAZ", "value": "SPETSNAZ-GLAZ"},
                             {"label": "SPETSNAZ-KAPKAN", "value": "SPETSNAZ-KAPKAN"},
                             {"label": "SPETSNAZ-TACHANKA", "value": "SPETSNAZ-TACHANKA"},
                             {"label": "SWAT-ASH", "value": "SWAT-ASH"},
                             {"label": "SWAT-CASTLE", "value": "SWAT-CASTLE"},
                             {"label": "SWAT-PULSE", "value": "SWAT-PULSE"},
                             {"label": "SWAT-THERMITE", "value": "SWAT-THERMITE"}],
                         multi=False,
                         value="None",
                         style={'width': '49%', 'display': 'inline-block'}
                         )
    ]),
    html.Div([
        dcc.Graph(id='delta_figure', figure={})
    ])