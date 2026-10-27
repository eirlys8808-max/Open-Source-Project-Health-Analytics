
# Technical Decision Log
## Open Source Project Health Analytics

This document records important technical and analytical decisions, their rationale, alternatives, and potential trade-offs.

## Decision 001 — Project Technology Stack

**Status:** Proposed

**Context:**

The project needs to collect repository data, clean and analyze it, query structured datasets, and communicate findings through an interactive dashboard.

**Decision:**

Use the following tools:

- Python for data collection and transformation.
- GitHub REST API as the initial data source.
- SQL for structured querying and analytical metrics.
- Power BI for dashboard development.
- Git and GitHub for version control and project collaboration.

**Rationale:**

This stack demonstrates an end-to-end Data Analytics workflow, from source data to business-oriented insights.

**Alternatives considered:**

- Manual data collection.
- Spreadsheet-only analysis.
- Other visualization platforms.

**Trade-offs:**

- API rate limits may restrict data collection.
- Data quality and missing values require validation.
- Power BI Desktop is a separate application.
- Database setup introduces additional complexity.

**Consequences:**

The project will use a modular structure so that collection, transformation, analysis, and visualization can be developed and tested separately.

---

## Decision 002 — Development Documentation

**Status:** Accepted

**Context:**

The project should document not only the final output but also the actual implementation process and technical challenges.

**Decision:**

Maintain three documents:

- `DEVELOPMENT_LOG.md`
- `TROUBLESHOOTING.md`
- `DECISIONS.md`

**Rationale:**

These documents preserve implementation history, verified fixes, and the reasoning behind technical choices.

**Consequences:**

Each development session should record its actions, results, issues, and next steps. Proposed decisions must be distinguished from decisions that have been implemented and verified.

---

## Decision Template

### Decision [Number] — [Title]

**Status:** Proposed / Accepted / Implemented / Superseded

**Date:**

**Context:**

**Decision:**

**Alternatives considered:**

**Rationale:**

**Trade-offs and risks:**

**Implementation evidence:**

**Consequences:**

**Review date:**
## Quyết định: Mở rộng phương pháp lấy mẫu repository

**Ngày:** 2026-10-27

### Vấn đề
Bộ dữ liệu ban đầu gồm 100 repository Python được chọn theo stars giảm dần. Mẫu thiên về repository nổi tiếng và chưa thể hiện tốt sự khác biệt về mức độ phổ biến.

### Quyết định
Mở rộng phân tích thành ba nhóm:
- Phổ biến cao: stars >= 100.000.
- Phổ biến trung bình: stars từ 10.000 đến 99.999.
- Phổ biến thấp hơn: stars từ 1.000 đến 9.999.

### Lý do
So sánh các nhóm có thể giúp nhận diện sự khác biệt về forks, open issues và thời gian cập nhật.

### Giới hạn
Các ngưỡng stars là lựa chọn phân tích, không phải tiêu chuẩn sức khỏe dự án. Cần lưu ý rằng việc so sánh các nhóm vẫn có thể chịu ảnh hưởng của loại dự án, tuổi đời và cách sử dụng GitHub.

### Nguyên tắc lưu dữ liệu
Không ghi đè bộ dữ liệu ban đầu khi thử nghiệm phương pháp lấy mẫu mới. Lưu bộ dữ liệu mở rộng vào file riêng để có thể tái lập và so sánh kết quả.