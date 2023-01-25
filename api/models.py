from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=120)
    carreer_start_date = models.DateField()
    place_of_origin = models.CharField(max_length=200)

    def create_artist():
        return Artist()


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    date_of_release = models.DateField(verbose_name="The date the album has been released.")
    total_duration = models.DurationField(verbose_name="Total duration of the album in minutes")
    number_of_songs = models.IntegerField(verbose_name="Number of the songs in the album.")
    album_cover = models.FilePathField(verbose_name="Path to the file wich contains the album cover")