document.addEventListener("DOMContentLoaded", function () {
    const reservationForm = document.getElementById("reservationForm");

    if (reservationForm) {
        reservationForm.onsubmit = function (event) {
            event.preventDefault(); // 기본 폼 제출 방지

            fetch(this.action, {
                method: "POST",
                body: new FormData(this)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("✅ 예약이 완료되었습니다!");
                    window.location.href = "/parking-lots/"; // ✅ 주차장 목록 페이지로 이동
                } else {
                    alert("❌ 오류: " + data.message);
                }
            })
            .catch(error => alert("서버 오류 발생: " + error));
        };
    }
});