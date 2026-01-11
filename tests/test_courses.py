from playwright.sync_api import expect, Page


def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title_page_course = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(title_page_course).to_have_text("Courses")

    text_no_results_page_course = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_no_results_page_course).to_have_text("There is no results")

    icon_no_results_page_course = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_no_results_page_course).to_be_visible()

    description_no_results_page_course = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(description_no_results_page_course).to_have_text("Results from the load test pipeline will be displayed here")