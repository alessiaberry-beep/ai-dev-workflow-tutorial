# Tasks: Sales Analytics Dashboard

**Input**: Design documents from `/specs/001-sales-analytics-dashboard/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, research.md, quickstart.md

**Tests**: No automated tests requested for Phase 1 (manual testing per plan.md)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `app.py` at repository root
- Data file: `data/sales-data.csv`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure with `src/` folder and `src/__init__.py`
- [ ] T002 Create `pyproject.toml` with dependencies (streamlit, pandas, plotly)
- [ ] T003 [P] Create `.gitignore` with Python and virtual environment exclusions
- [ ] T004 [P] Create `README.md` with project overview and setup instructions
- [ ] T005 Initialize virtual environment using `uv venv` and install dependencies

**Checkpoint**: Project structure ready, dependencies installed

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 Implement `load_sales_data()` function in `src/data_loader.py` with CSV loading, date parsing, and type validation
- [ ] T007 Add error handling in `src/data_loader.py` for missing file and empty data scenarios (FR-011)
- [ ] T008 Create basic `app.py` Streamlit skeleton with page configuration and title
- [ ] T009 Add data loading call in `app.py` with `@st.cache_data` decorator for performance
- [ ] T010 Implement error display in `app.py` showing user-friendly messages when data loading fails

**Checkpoint**: Foundation ready - data loads successfully, errors handled gracefully

---

## Phase 3: User Story 1 - View Business Performance at a Glance (Priority: P1) 🎯 MVP

**Goal**: Display Total Sales and Total Orders KPIs prominently at the top of the dashboard

**Independent Test**: Open dashboard and verify Total Sales shows as currency (e.g., "$687,432") and Total Orders shows as formatted number (e.g., "482")

### Implementation for User Story 1

- [ ] T011 [US1] Add `calculate_total_sales()` function in `src/data_loader.py` returning sum of total_amount column
- [ ] T012 [US1] Add `calculate_total_orders()` function in `src/data_loader.py` returning count of rows
- [ ] T013 [US1] Add `format_currency()` helper function in `src/data_loader.py` for US dollar formatting
- [ ] T014 [US1] Add `format_number()` helper function in `src/data_loader.py` for thousands separators
- [ ] T015 [US1] Implement KPI display section in `app.py` using `st.metric()` for Total Sales
- [ ] T016 [US1] Implement KPI display section in `app.py` using `st.metric()` for Total Orders
- [ ] T017 [US1] Add loading state handling in `app.py` using `st.spinner()` during data processing

**Checkpoint**: User Story 1 complete - KPIs display correctly with proper formatting

---

## Phase 4: User Story 2 - Analyze Sales Trends Over Time (Priority: P2)

**Goal**: Display a line chart showing monthly sales trends over the 12-month period

**Independent Test**: View trend chart and verify it shows 12 months of data with interactive tooltips displaying exact values on hover

### Implementation for User Story 2

- [ ] T018 [US2] Add `aggregate_monthly_sales()` function in `src/data_loader.py` grouping by month and summing total_amount
- [ ] T019 [US2] Create `src/charts.py` with `create_trend_chart()` function using Plotly Express line chart
- [ ] T020 [US2] Configure trend chart with proper title "Sales Trend Over Time" and axis labels in `src/charts.py`
- [ ] T021 [US2] Add hover template to trend chart showing formatted date and currency value in `src/charts.py`
- [ ] T022 [US2] Integrate trend chart in `app.py` below KPIs using `st.plotly_chart()`

**Checkpoint**: User Story 2 complete - trend chart displays monthly sales with tooltips

---

## Phase 5: User Story 3 - Compare Sales by Product Category (Priority: P3)

**Goal**: Display a bar chart showing sales by category, sorted highest to lowest

**Independent Test**: View category chart and verify all 5 categories (Electronics, Accessories, Audio, Wearables, Smart Home) appear sorted by value with tooltips

### Implementation for User Story 3

- [ ] T023 [US3] Add `aggregate_category_sales()` function in `src/data_loader.py` grouping by category and sorting descending
- [ ] T024 [US3] Add `create_category_chart()` function in `src/charts.py` using Plotly Express bar chart
- [ ] T025 [US3] Configure category chart with title "Sales by Category" and axis labels in `src/charts.py`
- [ ] T026 [US3] Add hover template to category chart showing category name and formatted currency in `src/charts.py`
- [ ] T027 [US3] Integrate category chart in `app.py` using `st.plotly_chart()` with `st.columns()` layout

**Checkpoint**: User Story 3 complete - category breakdown displays all 5 categories sorted

---

## Phase 6: User Story 4 - Compare Sales by Region (Priority: P4)

**Goal**: Display a bar chart showing sales by region, sorted highest to lowest

**Independent Test**: View regional chart and verify all 4 regions (North, South, East, West) appear sorted by value with tooltips

### Implementation for User Story 4

- [ ] T028 [US4] Add `aggregate_region_sales()` function in `src/data_loader.py` grouping by region and sorting descending
- [ ] T029 [US4] Add `create_region_chart()` function in `src/charts.py` using Plotly Express bar chart
- [ ] T030 [US4] Configure region chart with title "Sales by Region" and axis labels in `src/charts.py`
- [ ] T031 [US4] Add hover template to region chart showing region name and formatted currency in `src/charts.py`
- [ ] T032 [US4] Integrate region chart in `app.py` alongside category chart using `st.columns()` layout

**Checkpoint**: User Story 4 complete - regional breakdown displays all 4 regions sorted

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements and deployment preparation

- [ ] T033 [P] Add consistent color scheme across all charts in `src/charts.py`
- [ ] T034 [P] Add type hints to all functions in `src/data_loader.py` and `src/charts.py`
- [ ] T035 Verify dashboard layout follows spec: KPIs → Trend → Category/Region side-by-side in `app.py`
- [ ] T036 [P] Create `requirements.txt` for Streamlit Community Cloud deployment
- [ ] T037 Run manual validation against quickstart.md checklist
- [ ] T038 Test dashboard in multiple browsers (Chrome, Firefox, Safari, Edge)

**Checkpoint**: Dashboard ready for deployment

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - US1 (P1): Can start immediately after Phase 2
  - US2 (P2): Can start after Phase 2 (independent of US1)
  - US3 (P3): Can start after Phase 2 (independent of US1, US2)
  - US4 (P4): Can start after Phase 2 (independent of US1, US2, US3)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: No dependencies on other stories - MVP target
- **User Story 2 (P2)**: No dependencies on US1 (uses same data loader)
- **User Story 3 (P3)**: No dependencies on US1/US2 (uses same data loader)
- **User Story 4 (P4)**: No dependencies on other stories; shares layout with US3

### Within Each User Story

1. Data aggregation function in `src/data_loader.py`
2. Chart creation function in `src/charts.py` (if applicable)
3. Integration in `app.py`

### Parallel Opportunities

- **Setup Phase**: T003, T004 can run in parallel
- **Foundational Phase**: T006, T007 are sequential (same file); T008-T010 sequential (same file)
- **After Phase 2**: All user stories (US1-US4) can start in parallel
- **Polish Phase**: T033, T034, T036 can run in parallel

---

## Parallel Example: After Foundational Phase

```bash
# Once Phase 2 is complete, these user stories can run in parallel:
Task: "T011-T017 [US1] KPI implementation"
Task: "T018-T022 [US2] Trend chart implementation"
Task: "T023-T027 [US3] Category chart implementation"
Task: "T028-T032 [US4] Region chart implementation"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T005)
2. Complete Phase 2: Foundational (T006-T010)
3. Complete Phase 3: User Story 1 (T011-T017)
4. **STOP and VALIDATE**: Dashboard shows KPIs correctly
5. Deploy/demo as MVP

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test KPIs → Deploy/Demo (MVP!)
3. Add User Story 2 → Test trend chart → Deploy/Demo
4. Add User Story 3 → Test category chart → Deploy/Demo
5. Add User Story 4 → Test region chart → Deploy/Demo
6. Polish → Final validation → Production deployment

### Single Developer Strategy

Execute in priority order:
1. Setup (Phase 1)
2. Foundational (Phase 2)
3. US1: KPIs (Phase 3) → Validate
4. US2: Trends (Phase 4) → Validate
5. US3: Categories (Phase 5) → Validate
6. US4: Regions (Phase 6) → Validate
7. Polish (Phase 7) → Deploy

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- All charts use Plotly for consistent interactivity
- Data caching via `@st.cache_data` improves performance
