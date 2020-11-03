from models.subscription import Subscription, subscription_schema, subscriptions_schema
from models.database import db, abort
from sqlalchemy.exc import SQLAlchemyError

def read_all():
  all_subs = Subscription.query.all()
  print(all_subs)
  return subscriptions_schema.dump(all_subs)

def read_one(email_or_discord_user_id):
  if '@' in email_or_discord_user_id:
    sub = Subscription.query.filter_by(email=email_or_discord_user_id).first()
  else:
    sub = Subscription.query.filter_by(discord_user_id=email_or_discord_user_id).first()

  if sub is None:
    abort(
      404, "Subscription with given email or discord user id not found"
    )

  return subscription_schema.dump(sub)

def create(subscription):
  email = subscription.get('email', None)
  discord_user_id = subscription.get('discord_user_id', None)

  if discord_user_id:
    existing = Subscription.query.filter_by(discord_user_id=discord_user_id).first()
  elif email:
    existing = Subscription.query.filter_by(email=email).first()
  else:
    # data for subscription missing
    abort(400, "data missing for subscription")

  if existing:
    abort(406, "Subscription with given email or discord user id already exists")

  try:
    sub = Subscription(email=email, discord_user_id=discord_user_id)
    print("add sub")
    db.session.add(sub)
    db.session.commit()
  except SQLAlchemyError as e:
    # TODO: use abort() here as well
    print("Failed to create subscription")
    print(e)
    abort(400, str(e.__dict__['orig']))

  return subscription_schema.dump(sub)

# def update(subscription):
#   email = subscription.get('email', None)
#   discord_user_id = subscription.get('discord_user_id', None)

#   if discord_user_id:
#     existing = Subscription.query.filter_by(discord_user_id=discord_user_id).first()
#   elif email:
#     existing = Subscription.query.filter_by(email=email).first()
#   else:
#     # data for subscription missing
#     abort(400, "data missing for subscription")

#   if existing is None:
#     abort(
#       404, "Subscription with given email or discord user id not found"
#     )
  



