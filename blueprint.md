# Blueprint: N-ơi Application

## I. Tổng quan

Đây là tài liệu kiến trúc và kế hoạch phát triển cho ứng dụng "N-ơi", một nền tảng học tập và phát triển bản thân được xây dựng trên nền tảng web hiện đại.

### Mục tiêu
- Xây dựng một ứng dụng Single Page Application (SPA) với giao diện người dùng hiện đại, đáp ứng.
- Tích hợp với Firebase để quản lý người dùng (Authentication), dữ liệu (Firestore), và các dịch vụ backend khác.
- Cung cấp trải nghiệm mượt mà, liền mạch cho người dùng trên cả desktop và mobile.

## II. Kiến trúc & Thiết kế

### 1. Giao diện người dùng (Frontend)
- **Nền tảng:** HTML, TailwindCSS, và JavaScript (Vanilla JS).
- **Cấu trúc:** Ứng dụng được xây dựng dưới dạng một file `index.html` duy nhất, chứa toàn bộ logic hiển thị và quản lý trạng thái.
- **Thiết kế:**
    - **Bố cục:** Sử dụng layout flexbox với sidebar điều hướng cố định bên trái và khu vực nội dung chính bên phải.
    - **Thẩm mỹ:** Phong cách thiết kế hiện đại, sạch sẽ với màu sắc ấm áp, font chữ dễ đọc (Be Vietnam Pro), và các hiệu ứng đổ bóng tinh tế để tạo chiều sâu.
    - **Tương tác:** Các thành phần có tính tương tác cao, với hiệu ứng hover, transition mượt mà.

### 2. Backend & Dữ liệu
- **Xác thực người dùng:** Sử dụng Firebase Authentication với phương thức đăng nhập qua Google (`signInWithPopup`).
- **Cơ sở dữ liệu:** Sử dụng Cloud Firestore để lưu trữ dữ liệu động của ứng dụng.
    - `communities`: Collection lưu trữ thông tin các cộng đồng/nhóm nhỏ.
        - `name`: Tên cộng đồng (String)
        - `mentor`: Tên người dẫn dắt (String)
        - `memberCount`: Số lượng thành viên (Number)
        - `price`: Phí tham gia (Number)
        - `icon`: Biểu tượng emoji cho cộng đồng (String)
    - `roadmap`: Collection lưu trữ thông tin các khóa học/lộ trình.
    - `users`: Collection lưu trữ thông tin người dùng.

## III. Kế hoạch Hiện tại: Tích hợp Firebase (Phase 1)

Đây là những bước đang được thực hiện để đưa ứng dụng vào trạng thái hoạt động cơ bản với backend thật.

### Bước 1: Kích hoạt tính năng Đăng nhập (Auth)
- **Công việc:** Tích hợp Firebase Auth SDK vào `index.html`.
- **Hành động:** Viết lại hàm `app.signIn()` để sử dụng `signInWithPopup` từ Firebase, cho phép người dùng đăng nhập bằng tài khoản Google thật.
- **Mục tiêu:** Khi người dùng nhấn nút "Tiếp tục với Google", một cửa sổ popup của Google sẽ hiện ra để xác thực.

### Bước 2: Thiết lập cấu trúc dữ liệu trên Firestore
- **Công việc:** Tạo "móng nhà" cho dữ liệu cộng đồng.
- **Hành động:** (Dành cho người dùng thực hiện) Vào Firebase Console, tạo collection `communities` với cấu trúc document như đã mô tả ở trên.
- **Mục tiêu:** Có một nơi để lưu trữ và truy vấn dữ liệu về các cộng đồng.

### Bước 3: Kết nối giao diện với cơ sở dữ liệu
- **Công việc:** Lấy và hiển thị dữ liệu động.
- **Hành động:**
    1. Tích hợp Firebase Firestore SDK.
    2. Viết hàm `app.fetchCommunities()` để truy vấn tất cả các document từ collection `communities`.
    3. Thay thế mảng `store.categories` tĩnh bằng dữ liệu từ Firestore.
    4. Cập nhật hàm `app.init()` và `app.signIn()` để gọi `fetchCommunities()` sau khi người dùng đăng nhập thành công.
    5. Sử dụng `onAuthStateChanged` để tự động đăng nhập người dùng nếu họ đã đăng nhập ở phiên trước.
- **Mục tiêu:** Dữ liệu các cộng đồng hiển thị trên trang "Học Tập" được lấy trực tiếp từ Firebase, không còn là dữ liệu hard-code.
