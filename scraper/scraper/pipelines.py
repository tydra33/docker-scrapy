# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from itemadapter import ItemAdapter
import psycopg2


class FlatsPipeline:
    def __init__(self):
        db_config = {
            "host": "docker-scrapy-database-1",  # not localhost
            "port": "5432",
            "database": "flats_db",
            "user": "postgres",
            "password": "ardit33",
        }

        self.connection = psycopg2.connect(**db_config)
        self.cur = self.connection.cursor()

        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS apartments (
            id serial PRIMARY KEY,
            title text,
            image_urls text
        )
        """
        )
        self.cur.execute(
            """
        DELETE FROM apartments *
        """
        )

    def process_item(self, item, spider):
        self.cur.execute(
            """ INSERT INTO apartments (title, image_urls) VALUES (%s,%s)""",
            (item["title"], str(item["image_urls"])),
        )

        self.connection.commit()

        return item
