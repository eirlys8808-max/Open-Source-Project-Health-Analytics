# Sổ tay học tập — Open Source Project Health Analytics

## Buổi học: [Tên nội dung]

**1. Hôm nay tôi thực hiện việc gì?**

Mô tả các thao tác đã thực hiện.

**2. Tôi học được gì?**

Giải thích bằng lời của mình, tránh chỉ sao chép định nghĩa.

**3. Tôi gặp vấn đề gì?**

Ghi lỗi, thao tác nhầm hoặc điều chưa hiểu.

**4. Vì sao vấn đề xảy ra?**

Phân biệt nguyên nhân đã xác minh với giả thuyết.

**5. Tôi đã giải quyết như thế nào?**

Ghi các bước xử lý và kết quả kiểm tra.

**6. Tôi có thể tự làm lại không?**

- [ ] Có thể tự làm mà không cần hướng dẫn.
- [ ] Làm được khi xem tài liệu.
- [ ] Cần người hướng dẫn hỗ trợ.

**7. Tôi tự đánh giá mức độ hiểu:** [1–5]

**8. Điều tôi cần ôn lại:**

**9. Bước tiếp theo:**


# Sổ tay học tập — Open Source Project Health Analytics


## Buổi 1: Khởi tạo dự án và thiết lập môi trường Python

### 1. Hôm nay tôi đã thực hiện việc gì?
- Tạo cấu trúc thư mục cho dự án phân tích sức khỏe các dự án mã nguồn mở.
- Tạo các file quản lý dự án và tài liệu ghi lại quá trình phát triển.
- Kiểm tra phiên bản Python và pip.
- Tạo môi trường ảo `.venv` và kích hoạt môi trường.
- Kiểm tra khả năng giải quyết các thư viện cần thiết bằng lệnh `pip install --dry-run`.
- Thực hành nhập lệnh trong PowerShell.

### 2. Tôi học được gì?
- **Python:** ngôn ngữ lập trình sẽ dùng để lấy dữ liệu từ GitHub API và xử lý dữ liệu.
- **pip:** công cụ cài đặt và quản lý thư viện Python.
- **Môi trường ảo `.venv`:** giúp cô lập các thư viện của dự án, tránh ảnh hưởng đến những dự án Python khác.
- **`requirements.txt`:** liệt kê các thư viện dự án cần sử dụng.
- **`--dry-run`:** cho phép kiểm tra phương án cài đặt mà chưa thực sự cài các thư viện.
- **PowerShell:** dấu nhắc lệnh hiển thị vị trí hiện tại và môi trường đang kích hoạt; không cần sao chép dấu nhắc này khi nhập lệnh.

### 3. Tôi đã gặp vấn đề gì?
Tôi đã sao chép cả dấu nhắc PowerShell, bao gồm `(.venv) PS ...>`, vào ô nhập lệnh. PowerShell báo lỗi `Unexpected token 'PS'`.

### 4. Nguyên nhân
Tôi nhầm phần hiển thị môi trường và thư mục hiện tại với nội dung lệnh cần thực thi.

### 5. Cách khắc phục
Chỉ nhập nội dung lệnh sau dấu `>` thay vì sao chép toàn bộ dấu nhắc PowerShell.

Lệnh cần chạy để cài thư viện:

`python -m pip install -r requirements.txt`

**Trạng thái:** Đã xác định cách nhập đúng. Cần xác nhận lệnh cài đặt thực sự chạy thành công trước khi kết luận môi trường đã sẵn sàng.

### 6. Tự đánh giá
- [ ] Tôi có thể tự tạo và kích hoạt môi trường ảo.
- [ ] Tôi hiểu sự khác nhau giữa Python, pip và `.venv`.
- [ ] Tôi biết cách cài thư viện từ `requirements.txt`.
- [ ] Tôi biết cách đọc lỗi cơ bản trong PowerShell.

**Mức độ hiểu của tôi (1–5):** ___

### 7. Điều cần ôn lại
- Cách kích hoạt môi trường ảo trên Windows.
- Cách cài đặt thư viện Python.
- Cách phân biệt dấu nhắc PowerShell với câu lệnh thực thi.

### 8. Bước tiếp theo
Cài đặt các thư viện dự án và kiểm tra xem chúng có thể được import trong Python hay không.
### 9. Kết quả kiểm tra môi trường Python

Tôi đã chạy lệnh kiểm tra khả năng import các thư viện và nhận được kết quả:

`All core libraries imported successfully!`

Các phiên bản thư viện đã kiểm tra:

| Thư viện | Phiên bản | Vai trò |
|---|---|---|
| requests | 2.34.2 | Gửi HTTP request để lấy dữ liệu từ GitHub API |
| pandas | 3.1.0 | Xử lý, làm sạch và phân tích dữ liệu dạng bảng |
| SQLAlchemy | 2.1.6 | Hỗ trợ tương tác với cơ sở dữ liệu bằng Python |

**Tôi hiểu được gì?**

Việc cài đặt thư viện và kiểm tra `import` là hai bước khác nhau. Cài đặt giúp đưa thư viện vào môi trường Python; kiểm tra `import` xác nhận chương trình có thể nạp thư viện đó.

**Tự đánh giá:** Tôi đã thực hiện được các lệnh kiểm tra cơ bản trong Terminal VS Code. Tôi cần tiếp tục thực hành để có thể tự xử lý lỗi môi trường và sử dụng các thư viện trong dự án thực tế.
## Buổi 2: Kết nối GitHub API bằng Python

### 1. Mục tiêu
Lấy dữ liệu thực tế của một repository từ GitHub API bằng thư viện `requests`.

### 2. Tôi đã thực hiện
- Tạo file `src/test_github_api.py`.
- Gửi yêu cầu đến API của repository `pandas-dev/pandas`.
- Nhận được HTTP status `200`.
- Đọc dữ liệu JSON và in ra tên repository, stars, forks, ngôn ngữ chính và thời điểm cập nhật.

### 3. Kiến thức đã học
- API cho phép chương trình giao tiếp với một dịch vụ bên ngoài.
- HTTP status `200` cho biết yêu cầu đã thành công.
- JSON là định dạng trao đổi dữ liệu phổ biến giữa các hệ thống.
- Python dictionary cho phép truy cập dữ liệu theo khóa.
- Dữ liệu từ API phản ánh thời điểm truy vấn và có thể thay đổi.

### 4. Liên hệ với dự án
Tôi có thể sử dụng GitHub API để thu thập dữ liệu của nhiều repository, sau đó dùng pandas để xử lý và phân tích các chỉ số hoạt động của dự án mã nguồn mở.

### 5. Tự đánh giá
- [ ] Tôi hiểu API là gì.
- [ ] Tôi hiểu ý nghĩa của HTTP status `200`.
- [ ] Tôi có thể giải thích `requests.get()` và `response.json()`.
- [ ] Tôi có thể tự viết lại chương trình lấy thông tin một repository.

**Mức độ hiểu của tôi (1–5):** ___

### 6. Câu hỏi cần tự trả lời
1. Điều gì xảy ra nếu API trả về status `404`?
2. Vì sao cần dùng `timeout=30`?
3. Vì sao số stars không đủ để kết luận sức khỏe của repository?
## Buổi 3: Thu thập nhiều repository từ GitHub API

### 1. Mục tiêu
Sử dụng GitHub Search API để tìm và thu thập dữ liệu của nhiều repository trong một lần gọi API.

### 2. Tôi đã thực hiện
- Tạo file `src/collect_repositories.py`.
- Tìm repository bằng điều kiện `language:Python stars:>1000`.
- Sắp xếp theo stars giảm dần.
- Giới hạn kết quả trả về ở 10 repository.
- Lấy tên, stars, forks, ngôn ngữ, số issue đang mở và thời gian cập nhật.

### 3. Kết quả
- HTTP status: 200.
- Tổng kết quả phù hợp do API báo cáo: 11.958.
- Số repository thực tế thu thập: 10.

### 4. Kiến thức đã học
- `params` giúp truyền các tham số tìm kiếm vào API.
- `per_page` giới hạn số kết quả trả về mỗi trang.
- `result["items"]` chứa danh sách repository trong phản hồi.
- Vòng lặp `for` giúp xử lý từng repository.
- `total_count` và số bản ghi thu thập được là hai khái niệm khác nhau.

### 5. Góc nhìn phân tích dữ liệu
Stars và forks có thể phản ánh mức độ quan tâm của cộng đồng, nhưng không đủ để kết luận sức khỏe dự án. Cần kết hợp nhiều chỉ số và xem xét bối cảnh của từng repository.

### 6. Tự đánh giá
- [ ] Tôi hiểu cách truyền tham số tìm kiếm cho API.
- [ ] Tôi hiểu cách xử lý danh sách bằng vòng lặp.
- [ ] Tôi phân biệt được tổng kết quả tìm kiếm với số bản ghi đã thu thập.
- [ ] Tôi có thể tự viết lại chương trình mà không sao chép nguyên mẫu.

**Mức độ hiểu của tôi (1–5):** ___

### 7. Bước tiếp theo
Chuyển dữ liệu thu thập được thành bảng và lưu thành file CSV để có thể phân tích bằng pandas.
## Buổi 4: Lưu dữ liệu thành CSV bằng pandas

### 1. Mục tiêu
Chuyển dữ liệu JSON từ GitHub API thành bảng và lưu thành file CSV.

### 2. Tôi đã thực hiện
- Sử dụng `pd.DataFrame(rows)` để tạo bảng dữ liệu.
- Sử dụng `Path` để xác định thư mục gốc của dự án.
- Tạo thư mục `data/raw` tự động nếu chưa tồn tại.
- Lưu 10 repository vào `data/raw/repositories.csv`.
- Kiểm tra kết quả bằng cách in `df.head()`.

### 3. Kết quả
- Số repository đã lưu: 10.
- Số cột: 6.
- Đường dẫn: `data/raw/repositories.csv`.
- Trạng thái: chương trình chạy thành công.

### 4. Kiến thức đã học
- DataFrame là cấu trúc dữ liệu dạng bảng của pandas.
- CSV là định dạng phổ biến để lưu dữ liệu dạng bảng.
- `index=False` giúp không ghi thêm chỉ mục của DataFrame thành một cột trong file.
- `Path(__file__).resolve()` giúp xác định đường dẫn dựa trên vị trí file Python.
- `df.head()` hiển thị 5 dòng đầu để kiểm tra nhanh dữ liệu.

### 5. Tự đánh giá
- [ ] Tôi hiểu cách chuyển danh sách dictionary thành DataFrame.
- [ ] Tôi hiểu cách lưu DataFrame thành CSV.
- [ ] Tôi biết cách xác định đường dẫn file đầu ra.
- [ ] Tôi có thể tự chạy lại chương trình và tìm file CSV.

**Mức độ hiểu của tôi (1–5):** ___

### 6. Bước tiếp theo
Đọc lại file CSV bằng pandas và kiểm tra kiểu dữ liệu, giá trị thiếu và các chỉ số cơ bản trước khi phân tích.
## Buổi 5: Kiểm tra chất lượng dữ liệu

### 1. Tôi đã thực hiện
- Kiểm tra số dòng và số cột.
- Kiểm tra giá trị thiếu và tên repository trùng lặp.
- Xem kiểu dữ liệu và thống kê mô tả.
- Chuyển `updated_at` sang kiểu ngày giờ UTC để kiểm tra.
- Kiểm tra các giá trị âm trong `stars`, `forks` và `open_issues`.

### 2. Kết quả
- 10 dòng, 6 cột.
- Không có giá trị thiếu trong dữ liệu đã thu thập.
- Không có tên repository trùng lặp.
- Không có ngày không hợp lệ.
- Không có giá trị âm trong ba cột số được kiểm tra.

### 3. Kiến thức đã học
- Kiểm tra chất lượng dữ liệu cần thực hiện trước khi phân tích.
- `pd.to_datetime()` giúp chuyển chuỗi thành ngày giờ.
- `errors="coerce"` giúp phát hiện ngày không hợp lệ.
- `isnull().sum()` đếm giá trị thiếu.
- `duplicated()` phát hiện bản ghi trùng lặp.
- Thống kê mô tả giúp nhận diện sự phân tán và các giá trị đáng chú ý.

### 4. Giới hạn của kiểm tra
Dữ liệu không có giá trị thiếu hoặc âm chưa có nghĩa là mọi dữ liệu đều chính xác. Cần kiểm tra thêm tính hợp lý của các chỉ số và bối cảnh của từng repository.

### 5. Tự đánh giá
- [ ] Tôi có thể giải thích các bước kiểm tra chất lượng dữ liệu.
- [ ] Tôi biết cách chuyển cột ngày giờ sang kiểu dữ liệu phù hợp.
- [ ] Tôi có thể đọc bảng thống kê mô tả.
- [ ] Tôi biết phân biệt dữ liệu hợp lệ về định dạng với dữ liệu đúng về mặt thực tế.

**Mức độ hiểu của tôi (1–5):** ___

### 6. Bước tiếp theo
Thực hiện phân tích khám phá dữ liệu (EDA), so sánh các repository theo stars, forks và số issue đang mở.
## Buổi 6: Phân tích khám phá dữ liệu (EDA)

### 1. Tôi đã thực hiện
- Tính trung bình và trung vị của stars, forks và open issues.
- Xếp hạng Top 5 repository theo stars, forks và open issues.
- Rút ra insight ban đầu từ dữ liệu.
- Tạo biểu đồ thanh ngang Top 10 Python repositories theo stars.
- Lưu biểu đồ tại `docs/top_repositories_by_stars.png`.

### 2. Kiến thức đã học
- `mean()` tính trung bình.
- `median()` tính trung vị.
- `nlargest()` tìm các giá trị lớn nhất.
- `sort_values()` sắp xếp dữ liệu.
- `matplotlib` tạo biểu đồ bằng Python.
- `plt.savefig()` lưu biểu đồ thành ảnh PNG.

### 3. Insight ban đầu
- Repository có nhiều stars nhất chưa chắc có nhiều forks nhất.
- Số open issues chênh lệch lớn giữa các repository.
- Trung bình có thể bị ảnh hưởng bởi các giá trị cực lớn.
- Không nên kết luận chất lượng dự án chỉ dựa vào số open issues.

### 4. Giới hạn phân tích
- Mẫu hiện tại chỉ có 10 repository.
- Dữ liệu được chọn theo stars nên có thiên lệch chọn mẫu.
- Stars, forks và open issues chưa đủ để đánh giá toàn diện sức khỏe dự án.
- Dữ liệu GitHub thay đổi theo thời gian.

### 5. Tự đánh giá
- [ ] Tôi hiểu sự khác nhau giữa trung bình và trung vị.
- [ ] Tôi biết cách xếp hạng repository bằng pandas.
- [ ] Tôi biết cách tạo và lưu biểu đồ bằng matplotlib.
- [ ] Tôi có thể giải thích ít nhất hai insight từ dữ liệu.

**Mức độ hiểu của tôi (1–5):** ___

### 6. Bước tiếp theo
Mở rộng dữ liệu và xây dựng các chỉ số phân tích có ý nghĩa hơn trước khi tạo dashboard Power BI.
## Buổi 7: Mở rộng dữ liệu và kiểm tra chất lượng

### 1. Tôi đã thực hiện
- Mở rộng dữ liệu từ 10 lên 100 repository Python.
- Chạy lại chương trình kiểm tra chất lượng dữ liệu.
- Tạo lại biểu đồ Top 10 repository theo stars.
- Ghi đè biểu đồ cũ bằng kết quả từ bộ dữ liệu mới.

### 2. Kết quả kiểm tra
- Số dòng: 100.
- Số cột: 6.
- Không có giá trị thiếu.
- Không có tên repository trùng lặp.
- Không có ngày cập nhật không hợp lệ.
- Không có giá trị âm trong stars, forks và open issues.

### 3. Kiến thức đã học
- `per_page` điều khiển số kết quả trả về trên mỗi trang của GitHub Search API.
- Có thể tái sử dụng cùng một script để phân tích dữ liệu mới.
- Cần kiểm tra chất lượng sau khi mở rộng dữ liệu.
- Biểu đồ được tạo lại từ CSV hiện tại khi chạy script.
- Trung bình và trung vị cung cấp góc nhìn khác nhau về phân bố dữ liệu.

### 4. Giới hạn
- Dữ liệu chỉ gồm các repository Python có hơn 1.000 stars.
- Dữ liệu hiện tại là một ảnh chụp tại thời điểm thu thập, chưa đủ để đo tốc độ tăng trưởng.
- Stars, forks và open issues chưa đủ để kết luận một dự án khỏe mạnh hay không.

### 5. Tự đánh giá
- [ ] Tôi biết cách tăng số lượng repository được thu thập.
- [ ] Tôi biết cách kiểm tra dữ liệu sau khi cập nhật.
- [ ] Tôi có thể tạo lại biểu đồ từ CSV.
- [ ] Tôi hiểu giới hạn của mẫu dữ liệu hiện tại.

**Mức độ hiểu của tôi (1–5):** ___

### 6. Bước tiếp theo
Thiết kế thêm các chỉ số phân tích và chuẩn bị dữ liệu có cấu trúc tốt hơn cho dashboard Power BI.