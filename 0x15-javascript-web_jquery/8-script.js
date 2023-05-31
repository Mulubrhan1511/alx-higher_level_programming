$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
  const movies = data.results;
  const movieList = $("<ul></ul>");
  $.each(movies, function(index, movie) {
    const title = $("<li></li>").text(movie.title);
    movieList.append(title);
  });
  $("ul#list_movies").replaceWith(movieList);
});