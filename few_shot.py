import pandas as pd
import json

class FewShotPosts:
    def __init__(self, file_path="data/new_processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.unique_fields = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.DataFrame(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            self.unique_tags = list(set(self.df['tags'].explode()))
            self.unique_fields = list(self.df['field'].unique())

    def get_filtered_posts(self, field, length, language, tag):
        df_filtered = self.df[
            (self.df['field'] == field) &
            (self.df['tags'].apply(lambda tags: tag in tags)) &
            (self.df['language'] == language) &
            (self.df['length'] == length)
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags

    def get_fields(self):
        return self.unique_fields

    def get_topics_by_field(self, field):
        field_posts = self.df[self.df['field'] == field]
        return list(set(field_posts['tags'].explode()))

if __name__ == "__main__":
    fs = FewShotPosts()
    print("Fields:", fs.get_fields())
    print("All Tags:", fs.get_tags())
    print("Topics for Marketing:", fs.get_topics_by_field("Marketing"))
    posts = fs.get_filtered_posts("Marketing", "Medium", "English", "Branding")
    print("Filtered Posts:", posts)