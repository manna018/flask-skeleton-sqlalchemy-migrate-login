from app import create_app,db
if __name__ == "__main__":
    fap=create_app('dev')
    with fap.app_context():
        db.create_all()
    
    fap.run(host='0.0.0.0', port=5000)

# Inserting using Python
# >>> from app import db
# >>> from app import create_app
# >>> fap=create_app('dev')
# >>> app_ctx=fap.app_context()
# >>> app_ctx.push()
# >>> db.create_all()
# >>> from app.catalog.models import Publication
# >>> pb=Publication(name='Oxford')
# >>> db.session.add(pb)
# >>> db.session.commit()
# >>> app_ctx.pop()

# use flask click instead