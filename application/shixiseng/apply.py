from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from driver.setup import setup_driver

'''
    param = {
        keyword: job_title, 
        city: city
    }
'''
def apply_shixiseng(param):
    print("Starting web driver...")
    driver = setup_driver()
    title = param['keyword']
    city = param['city']
    print("Fetching job page...")
    driver.get(f"https://www.shixiseng.com/interns?page=1&type=school&keyword={title}&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city={city}&internExtend=")

    wait = WebDriverWait(driver, 10)

    page_num = 1
    while True:
        print(f"Processing page {page_num}")
        
        # Wait for page to load and find all job links
        time.sleep(3)
        job_links = driver.find_elements(By.CSS_SELECTOR, ".f-l.intern-detail__job p a")
        
        # Apply to each job
        for i, job_link in enumerate(job_links):
            print(f"Applying to job {i+1}/{len(job_links)} on page {page_num}")
            
            # Store original window handle
            original_window = driver.current_window_handle
            
            step = 0
            try:
                # Click job link
                job_link.click()

                # Switch to new page that opens
                driver.switch_to.window(driver.window_handles[-1])

                # Click apply button
                time.sleep(2)
                apply_btn = driver.find_element(By.CSS_SELECTOR, ".btn-box.resume_apply.com_res")
                apply_btn.click()
                
                step = 1

                # Switch to new page that opens
                driver.switch_to.window(driver.window_handles[-1])

                # Wait for resume selection image and confirm button to appear
                attachment_resume_img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[src="https://sxsimg.xiaoyuanzhao.com/static/img/deliver-layer/radio-choose.png"]')))
                confirm_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.common-deliver__footer .btn')))

                # Click resume selection image
                attachment_resume_img.click()

                # Click confirm button
                confirm_btn.click()

                # # Click batch apply button
                # batch_apply_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-button.submit-btn.el-button--default")))
                # batch_apply_btn.click()

                # # Wait and click final confirmation
                # time.sleep(2)
                # final_confirm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".result-confirm")))
                # final_confirm.click()
                
                print(f"Successfully applied to job {i+1}")
                
            except Exception as e:
                if step == 0:
                    print(f"Already applied to job {i+1}")
                else:
                    print(f"Failed to apply to job {i+1}")
            
            finally:
                # Close current window and return to original list
                if len(driver.window_handles) > 1:
                    driver.close()
                driver.switch_to.window(original_window)
                time.sleep(1)

        print(f"Finished applying to all jobs on page {page_num}")
        
        # Check if next button exists and is not disabled
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-next")
            if next_btn.get_attribute("disabled") is not None:
                print("Reached last page. Job finished!")
                break
            else:
                print("Going to next page...")
                next_btn.click()
                page_num += 1
                time.sleep(3)  # Wait for next page to load
        except Exception as e:
            print("Next button not found or error occurred. Job finished!")
            break
    print("All pages processed!")
    driver.quit()