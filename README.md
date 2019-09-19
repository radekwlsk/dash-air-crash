# dash-air-crash

Simple [Dash](https://dash.plot.ly/) app created to present basics about the framework during presentation.

> Dash is a productive Python framework for building web applications.
> 
> Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.
>
> Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build an interactive web-based application. Dash is simple enough that you can bind a user interface around your Python code in an afternoon.
>
> Dash apps are rendered in the web browser. You can deploy your apps to servers and then share them through URLs. Since Dash apps are viewed in the web browser, Dash is inherently cross-platform and mobile ready.

Data presented is taken from [Socrata's](https://opendata.socrata.com/Government/Airplane-Crashes-and-Fatalities-Since-1908/q2te-8cvq) opendata API. It contains details about _Airplane Crashes and Fatalities Since 1908_ (up to 2009).

Project is gradually extended with more and more features of Dash, each step is available as it's own tag:

 - `1-basic` - basic setup with docker,
 - `2-html` - shows usage of HTML tags as `dash_html_components`,
 - `3-styles` - presents ability to style the page (using inline styles),
 - `4-markdown` - Markdown support with `dash_core_components.Markdown`,
 - `5-ext-css` - linking external css files,
 - `6-assets` - buildin local assets support in `assets/` directory,
 - `7-dataset` - presenting dataset (taken from Socrata API),
 - `8-datatable` - display the data in `dash_table.DataTable` supporting filtering and ordering out-of-the-box,
 - `9-graph` - presenting data on a Plotly graph using `dash_core_components.Graph` and `plotly` library,
 - `10-map` - dynamic modification of the Plotly graph with Dash callbacks.

To learn more about those concepts please visit:

- [Dash User Guide](https://dash.plot.ly/),
- [The Dash Community Forum](https://community.plot.ly/c/dash),
- [Plotly Python Open Source Graphing Library](https://plot.ly/python/).


## Usage

First you have to create `.env` file in the root directory of the project (where `docker-compose.yml` is), providing following variables:
```
SOCRATA_API_URL=opendata.socrata.com
SOCRATA_AIRCRASHES_DATASET_ID=q2te-8cvq

GOOGLE_API_KEY=<google-maps-api-key>
```
where `<google-maps-api-key>` should be replaced by your Google Maps API key, which is used to get coordinates of crash sites used in `10-map` tag. If you don't want to provide that skip the last tag.


App is dockerized, to run the local dev server simply run (you need to have `docker-compose`, instructions [here](https://docs.docker.com/compose/install/)):

```bash
$ docker-compose up
```

It will start the server at [`http://localhost:8050`](http://localhost:8050).

Stop it with:

```bash
$ docker-compose down
```
