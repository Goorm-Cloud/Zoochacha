from services.reservation_service.__init__ import create_app  # ✅ 정확한 경로 지정

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)