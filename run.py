from app import create_app
if __name__ == "__main__":
    fap=create_app('dev')
    fap.run(host='0.0.0.0', port=5000)