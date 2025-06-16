from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    firstname:Mapped[str] = mapped_column(String(50),nullable=False)
    lastname:Mapped[str] = mapped_column(String(50),nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            'username':self.username,
            'firstname':self.firstname,
            'lastname':self.lastname
        }

class Post(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    

    def serialize(self):
        return{
            'id':self.id,
            'user_id':self.user_id
        }
    
class Follower(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    user_from_id:Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    user_to_id:Mapped[int] = mapped_column(db.ForeignKey('user.id'))


    def serialize(self):
        return{
            'id':self.id,
            'user_from_id':self.user_from_id,
            'user_to_id':self.user_to_id
        }
    
class Media(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    type:Mapped[str] = mapped_column(String(20),nullable=False)
    url:Mapped[str] = mapped_column(String(300),nullable=False)
    post_id:Mapped[int] = mapped_column(db.ForeignKey('post.id'))


    def serialize(self):
        return{
            'id':self.id,
            'type':self.type,
            'url':self.url,
            'post_id':self.post_id
        }
    
class Comment(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    comment_text:Mapped[str] = mapped_column(String(500),nullable=False)
    author_id:Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    post_id:Mapped[int] = mapped_column(db.ForeignKey('post.id'))


    def serialize(self):
        return{
            'id':self.id,
            'comment_text':self.comment_text,
            'author_id':self.author_id,
            'post_id':self.post_id
        }
