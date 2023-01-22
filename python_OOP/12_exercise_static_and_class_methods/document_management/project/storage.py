from project import Category
from project import Document
from project import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        searched_category = [x for x in self.categories if x.id == category_id][0]
        searched_category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        searched_topic = [x for x in self.topics if x.id == topic_id][0]
        searched_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        searched_document = [x for x in self.documents if x.id == document_id][0]
        searched_document.edit(new_file_name)

    def delete_category(self, category_id):
        self.categories = [x for x in self.categories if x.id != category_id]

    def delete_topic(self, topic_id):
        self.topics = [x for x in self.topics if x.id != topic_id]

    def delete_document(self, document_id):
        self.documents = [x for x in self.documents if x.id != document_id]

    def get_document(self, document_id):
        searched_document = [x for x in self.documents if x.id == document_id][0]
        return repr(searched_document)

    def __repr__(self):
        return '\n'.join(repr(x) for x in self.documents)