from Base_SpotifyAPI_Class import *


class FeaturesSpotifyAPI(SpotifyAPI):
    def __init__(self, client_id, client_secret, artists):
        super().__init__(client_id, client_secret)
        self.country_code = 'US'
        self.artists = artists
        self.artist_ids = []
        self.track_ids = []
        self.headers = None
        self.top_tracks = []  # top_tracks is a list of dictionaries, each dictionary having basic info about a song. There are 10 such dictionaries for each artist.
        # Note that top_tracks doesn't have cool audio features (just the basic ones)

        self.top_track_features = []  # has only the cool audio features
        self.top_track_details = []  # combination of basic and cool audio features
        self.df = []

    def auth(self):
        r = requests.post(self.token_url, data=get_token_data(), headers=self.get_token_headers())
        if r.status_code not in range(200, 299):
            raise Exception("Something went wrong.\n[Status Code] {r.status_code}")
        else:
            data = r.json()
            now = dt.datetime.now()
            access_token = data['access_token']
            expires_in = data['expires_in']
            self.access_token = access_token
            self.access_token_expires = now + dt.timedelta(seconds=expires_in)
            self.access_token_did_expire = self.access_token_expires <= now
            self.headers = {'Authorization': f'Bearer {access_token}'}
            print('Authorised\n')
            return access_token

    def get_artist_ids(self):
        print("Getting Artist IDs")
        artist_ids = []
        for artist in self.artists:
            data = urlencode({'q': artist, 'type': 'artist'})
            endpoint = f'https://api.spotify.com/v1/search?{data}'
            r = requests.get(endpoint, headers=self.headers)
            # pp(r.json())
            id_ = r.json()['artists']['items'][0]['id']
            artist_ids.append(id_)
            self.artist_ids = artist_ids
        print('Got Artist IDs\n')
        return self.artist_ids

    def get_top_tracks(self):
        print("Getting Top Tracks")
        for index, artist_id in enumerate(self.artist_ids):
            endpoint = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={self.country_code}'
            r = requests.get(endpoint, headers=self.headers)
            # pp(r.json())
            for d in r.json()['tracks']:
                # pp(d)
                d['album_name'] = d['album']['name']
                d['album_release_date'] = d['album']['release_date']
                d['album_type'] = d['album']['album_type']
                d['duration_sec'] = round(d['duration_ms'] / 1000, 1)
                d['explicit'] = str(d['explicit'])
                to_del = map(str,
                             'type track_number artists album duration_ms disc_number external_ids external_urls uri is_local is_playable href preview_url'.split())
                for x in to_del:
                    del d[x]
                d['artist'] = self.artists[index]
                self.track_ids.append(d['id'])
                self.top_tracks.append(d)
        # pp(self.track_ids)
        print("Got Top Tracks\n")
        return self.top_tracks

    def get_top_track_features(self):
        print("Getting Features for Top Tracks")
        counter = 0
        print('[1]')
        for index, id_ in enumerate(self.track_ids):
            if counter == 60:
                time.sleep(10)
                counter = -20
            endpoint = f"https://api.spotify.com/v1/audio-features/{id_}"
            r = requests.get(endpoint, headers=self.headers)
            d = r.json()
            try:
                to_del = map(str, 'analysis_url uri duration_ms track_href type'.split())  # this line glitches sometime when uri is included in the map object
                for x in to_del:
                    del d[x]
            except Exception as e:
                print(str(e))

            # analysis_url
            # del d['duration_ms']
            # del d['track_href']
            # del d['type']
            counter += 1
            self.top_track_features.append(d)

            # To show us the progress
            if (index + 1) % 50 == 0:
                print(f'[{index + 1}]')
        print("Got Features for Top Tracks\n")
        return self.top_track_features

    def get_combined(self):
        top_track_features_copy = self.top_track_features.copy()
        top_track_details = self.top_tracks.copy()
        for i in range(len(top_track_details)):
            top_track_details[i].update(top_track_features_copy[i])
        self.top_track_details = top_track_details
        return self.top_track_details

    def get_df(self):
        self.df = DF(self.top_track_details)
        return self.df
