from backend.app import create_app
brfc = create_app()
# set as PYTHONPATH the backend folder
if __name__ == "__main__":
    brfc.run(host='0.0.0.0', port=2323)
