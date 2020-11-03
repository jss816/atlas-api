from .database import db, ma

class Subscription(db.Model):
  __tablename__ = 'subscriptions'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100))
  discord_user_id = db.Column(db.String(100))
  created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
  cancelled_at = db.Column(db.TIMESTAMP, nullable=True)

  def __init__(self, email, discord_user_id):
    self.email = email
    self.discord_user_id
  
  def __repr__(self):
    return '<User %r>' % self.email

class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Subscription

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)