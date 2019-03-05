from .shared import db

class RecordedVideo(db.Model):
    __tablename__ = "RecordedVideo"
    id = db.Column(db.Integer,primary_key=True)
    videoDate = db.Column(db.DateTime)
    owningUser = db.Column(db.Integer,db.ForeignKey('user.id'))
    channelName = db.Column(db.String(255))
    channelID = db.Column(db.Integer,db.ForeignKey('Channel.id'))
    description = db.Column(db.String(2048))
    topic = db.Column(db.Integer)
    views = db.Column(db.Integer)
    length = db.Column(db.Float)
    videoLocation = db.Column(db.String(255))
    thumbnailLocation = db.Column(db.String(255))
    pending = db.Column(db.Boolean)
    upvotes = db.relationship('videoUpvotes', backref='recordedVideo', lazy="joined")

    def __init__(self, owningUser, channelID, channelName, topic, views, videoLocation, videoDate):
        self.videoDate = videoDate
        self.owningUser=owningUser
        self.channelID=channelID
        self.channelName=channelName
        self.topic=topic
        self.views=views
        self.videoLocation=videoLocation
        self.pending = True

    def __repr__(self):
        return '<id %r>' % self.id

    def get_upvotes(self):
        return len(self.upvotes)

    def serialize(self):
        return {
            'id': self.id,
            'channelID': self.channelID,
            'owningUser': self.owningUser,
            'videoDate': str(self.videoDate),
            'videoName': self.channelName,
            'topic': self.topic,
            'views': self.views,
            'length': self.length,
            'upvotes': self.get_upvotes(),
            'videoLocation': '/videos/' + self.videoLocation,
            'thumbnailLocation': '/videos/' + self.thumbnailLocation
        }