from h2o_wave import site, ui, app, main, Q
import pickle
from movie_helpers import fetch_poster, recommend

@app('/demo')
async def serve(q: Q):
    if not q.app.initialized:
        q.app.movies = pickle.load(open("Models/movies_list.pkl", 'rb'))
        q.app.similarity = pickle.load(open("Models/similarity.pkl", 'rb'))
        q.app.movies_list = q.app.movies['title'].values
        q.app.carousel_pos = 0
        q.app.initialized = True
        
    # Define screen_width here to ensure it's always defined before use
    screen_width = q.client.screen_width if q.client.screen_width is not None else 1024 
    
    # Set the page title and favicon
    q.page['meta'] = ui.meta_card(
        box='',
        title='My Custom Movie Recommender',
    )

    if q.args.show_recommend:
        q.app.movie_names, q.app.movie_posters = recommend(q.args.select_movie, q.app.movies, q.app.similarity)
        
        movie_cards = []  # Initialize an empty list to store each movie's UI components

        for name, poster in zip(q.app.movie_names, q.app.movie_posters):
            # Create a mini-card for each movie with the movie name above the poster
            movie_card = [
                ui.text_xl(name),  # Movie name
                ui.image(title=name, path=poster, width='200px')  # Movie poster with specified width
            ]
            movie_cards.append(ui.inline(items=movie_card, direction='column'))

        # Display the horizontally aligned movie cards under the search form
        q.page['recommendations'] = ui.form_card(
            box='1 4 -1 6',
            items=[ui.inline(items=movie_cards, justify='start')]
        )
    else:
        q.page['header'] = ui.header_card(
            box='1 1 -1 1',
            title='Movie Recommender System',
            subtitle='Select a movie to get recommendations',
            icon="Document",
            icon_color="green",
            items=[
                ui.link(
                    name="github_btn",
                    path="",
                    label="GitHub",
                    button=True,
            ),
        ],
            
        )

        dropdown = ui.dropdown(
            name='select_movie',
            label='Select Movie',
            choices=[ui.choice(name=m, label=m) for m in q.app.movies_list],
            value=q.app.movies_list[0] if len(q.app.movies_list) > 0 else ''
        )
        button = ui.button(name='show_recommend', label='Show Recommendations', primary=True)
        form_layout = '1 2 -1 3' if screen_width >= 720 else '1 2 -1 4'
        q.page['form'] = ui.form_card(box=form_layout, items=[dropdown, button])
        
        
    q.page['footer'] = ui.footer_card(
        box='5 -3 -1 1',
        caption='Powered by H2O Wave. For more awesome projects, visit our <a href="https://github.com/h2oai/wave" target="_blank">GitHub</a>.'
    )

    await q.page.save()
