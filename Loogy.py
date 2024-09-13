import streamlit as st
import pandas as pd

# Function to save the updated DataFrame back to CSV
def save_file(df, file_path):
    df.to_csv(file_path, index=False)

# Main app
def main():
    global pivot_table, df, filtered_df, last_record_df, last_5_records_df, app_remove_df, non_app_remove_df, event_flow_df, last_5_valid_records_df, last_5_records_df1, last_5_records_df2, col1
    #st.title("Analysis of Loogy Events Data 📉")
    st.markdown(
            """
            <style>
            .stApp {
                background-image: url('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ8NDQ0NFREWFhURFRUYHSggGBolGxUVITEhJSkrLi46Fx8/OD8tNygtLisBCgoKDg0NDw8NDysZFRkrKys3LTcrKzctLS0rKysrKys3LTcrLSs3LTc3LS0tNy0rNzcrNy03LSsrLSsrKysrK//AABEIAKgBLAMBIgACEQEDEQH/xAAZAAADAQEBAAAAAAAAAAAAAAABAgMABAX/xAAaEAEBAQEBAQEAAAAAAAAAAAAAAQISEQMT/8QAGgEAAwEBAQEAAAAAAAAAAAAAAAECAwQFBv/EABcRAQEBAQAAAAAAAAAAAAAAAAABEQL/2gAMAwEAAhEDEQA/APYkNI0NI73jxpD5gZimcprblsxSZbMUzlFb8hMqTIzKkym10cwkyeZPMmmU62kTmR5VmTTKdayI8twvwPBa0kc/DcOnhuC1Ucv5h+br4DgapyX5lvzdlwW4LVOS/Mt+bsuCXA0OS4C5dVwW4PQ5uQuV7gtyekhchYvcluTJC5Jcr3JLk0o2EsXsJcqTULC2K2EsMkrC1SwliomlAaBpdkh5AkPmLr5/k2YpmBmK5ia34HOVM5bOVc5Z2unkM5Uzkc5VzlNro5JMnmT5ypnKLW3KcwaYVmDzKbWsRmB4WmR5LVI8Dwty3JaeocNwvy3Jaeua4C4dNyHA0a5bgtw6rktyNPXLcEuHXcEuT09clwS4ddwS4PRrluSXLq1hO5VKTmuSXLpuU7lSXPck1HRrKesqJz6idjo1E9RUTUNROxfUS1FRNSoHsKpDtzFcwmYtiKrwOT5iuYXEWzGddPBs5VzkMxXOWdrq5HOVM5HOVM5RXRyGcqZybOVJlNrWEmTzJ5kZE60lJyPKnjeEZOW5U8Hwgly3KvgeEEuQuVuQ5GjULkty6LktyY1z3Jbl0XJLkHrnuSXDpuSXJnrluSay6rlPWVSjXLrKWsuvWUtZVCcusp6y6dZT1lRObUS1HTqI6i4moaiWovqJ6i4lz6hVNQnikPQxFsRLEdGIdeFwfEXxE8RfEZV1cHxFs5LiLYyiunkc5WzkMxXMZ2t+Wzk8gyHkS1hZDSGkHwlF8Hw3jeEYeN4ZgC+N4bxkgnjeG8bwwnYFingWAJWFuVbC2GNRuS3K1hbDPULlPWXRYSwz1zaylrLq1EtZVA5dZS1l1ayjrK4Vc2ojqOnUR1FRNc2olqOjcR3FxNc+4nVtxKria9HEdGIjiOjEFeHwriL4iWIviM66uFcRbEJiLZjKunk+YrmFzFMorfk0hpAhpEtIMgsJKDwRYAGFgYMLAAAtQRQsNQAKWw9AEnYWxSwthmnYSxWwthhDUT1F9RPUVDc+ojuOnUR3FQObcQ3HVuIbi4Vc24huOncQ2uIrn3EbF9pWLia9HEdGIjiOjA6eLwthfERwvhlXXwthfKOFss66OVcqRPKkRW0PDQsNEtIaCAkpmZgGZmBszMCYGYEDCBgKAgCClsMFAJS09LTNLUT0rU9Kho6iO4vpLaoHPuIbjo2htcJz7iG3RtDbSJrn2jV9o1cTXpYdGEML4KvH4XwvhDC2GddXC+FsoZWzWddHK2VIjmqZqK1isNE5TypXDwYWCShZmI2ZmAZmABmZjJgEATAIGC0KNCgFpaalpmTSej6T0qQ09I7V0jtUCW0NrbR2uEhtDa+0dria59o1faVXEV6OFsI5WwVeTwvhXKOVcorp5XzVc1DNUzUV0cr5qkqGapKixrFpTyoynlTY0isoyklGVOKUYso+kDMHrAmZmAZmAAQZgQANLTDBWtLaoBaWtaTVPDDVS1Taqeqoy6qO6pqpaqoE9IaV0ltUJHaO1tI7XEVDaVV0nVxFehlXKWVMlXl8r5qmajmqZqLHRyvmqZqGapKit+V808qMp5U2NotKeVGU0qcaRaU0qU0aUsUrKaVKUfSw1fW9T9N0WEf1iej6WAzel9D0YDeh6HpfTwsN6W0LS2nh4NpbQtLarBg2p6rWktPDbVT1RtT1VAuqnqm1U9VUImqlqn1UtVUTU9I7V0jpUTUtJ1TRKpnXfDwkPA82KZquahlTNTW3K0qmajmnzUWN+VpTypSmlLG3K0ppUpTSpxpFZTSoym9LGkVmjSoyj0WGt0PSU0PRYeK9D0j0PQwsV6DpPoOhgxX0t0TovQwYpdFuiXRbo8PD3Rbot0W08A2ltC0tp4GtJa1pLVJDVT1R1SapyEXVS1TaqeqpNT1UtKaT0qIqdJVKSqQ7oaMwebDQ8rMlrypKeVmS25PKeVmS25NKaVmJrDSj6zE0g+t6LEuN63QsDbpumYG3TdMwAdB0zAB6FrMYD0trMCC0trMZEtJazGklqeqzKJPVT1WY0VOk0DKRS0lBjQ//2Q==');            
                background-size: cover; /* Adjusts the size to cover the entire container */
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    st.sidebar.markdown(
            """
            <div style="text-align: center; padding: 10px;">
                <img src="https://play-lh.googleusercontent.com/1aLb6LSJjOQD2Yw3K7hNNyF_nuSoG-_OpsyXAyGXcY7y7r9lykrTTuToFnl2hR9VYE8"alt="Sidebar Image" style="max-width: 70%; height: auto;">
            </div>
            """,
            unsafe_allow_html=True
        )

    # File upload in the sidebar
    st.sidebar.title("File Upload")
    file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
    if file is None:
        # Show this title when no file is uploaded
        st.title("Analysis of Loogy Events Data 📉")
    else:
        # After file is uploaded, change title
        st.title("Analysis of User Removal and Churn Events in the Loogy App 🖌️")



    # List of events to filter out
    excluded_events = [
        "api_login_started", "check_google_response_not_purchased", "api_config_started",
        "api_call_dashboard_content", "api_trending_started", "api_call_main_category_dashboard",
        "api_main_category_list_started", "api_data_loaded_main_category_dashboard", "api_trending_success",
        "int_ad_loaded", "reward_ad_loaded", "ad_value", "api_font_started",
        "api_create_new_started", "api_font_success", "api_create_new_success", "api_ad_list_started",
        "api_show_referrer_started", "api_ad_list_success", "tag_selection_screen_visible", "tag_selection_next",
        "api_ai_generate_img_started", "api_ai_img_started", "api_ai_chat_edit_text_started",
        "api_bg_gradient_color_started", "api_seen_template_started", "api_bg_category_started",
        "api_download_zip_started", "api_download_zip_success", "api_bg_gradient_color_success",
        "api_ai_chat_edit_text_success", "api_ai_img_success", "api_search_data_started",
        "api_search_data_success", "api_search_result_started", "api_search_result_success",
        "api_category_data_started", "api_category_data_success", "api_bg_list_started", "api_bg_search_started",
        "api_social_media_started", "api_logo_started", "api_invitation_started", "api_edit_name_started",
        "api_ad_click_count_started", "api_generate_ai_text_started", "api_flyer_started", "api_flyer_success",
        "api_response_error_login_content", "API_response_error_config_content", "api_youtube_link_started",
        "api_youtube_link_success", "api_visiting_started", "api_icon_category_started", "api_icon_list_started",
        "api_effect_started", "api_ai_chat_deduct_xp_started", "api_ai_chat_deduct_xp_success",
        "api_ai_img_data_started", "api_you_may_like_started", "api_you_may_like_success",
        "api_ai_img_data_success", "editing_ai_chat_improve", "api_collect_referral_started",
        "api_festival_started", "api_festival_success", "api_update_xp_started", "api_update_xp_success",
        "api_daily_pick_you_may_like_started", "api_daily_pick_you_may_like_success",
        "api_subscription_data_started", "api_subscription_data_success", "api_subscription_verify_data_started",
        "api_subscription_verify_data_success", "api_ai_img_deduct_xp_started", "ai_total_api_calls",
        "app_clear_data", "api_ai_poster_deduct_xp_started", "os_update", "api_ai_chat_history_started",
        "api_ai_chat_history_success", "user_engagement","api_data_loaded_dashboard_content"
    ]

    second_event_list = [
        "abstract_bg_clicked", "abstract_bg_used", "ad_failed_to_show", "ad_not_available", "ad_reward",
        "add_img_btn", "addtext_btn", "ai__category_selected", "ai_avatar_category_selected", "ai_avatar_couple_selected",
        "ai_avatar_female_selected", "ai_avatar_generated_successfully", "ai_avatar_male_selected", "ai_avatarai_category_selected", "ai_avatarai_generated_successfully",
        "ai_avataraÄ±_generated_successfully", "ai_background_category_selected", "ai_backgroundai_category_selected", "ai_backgroundai_generated_successfully", "ai_barberai_category_selected",
        "ai_barberai_generated_successfully", "ai_caption_category_selected", "ai_celebratingideas_category_selected", "ai_chat_avatarai_catgory_selected", "ai_chat_btn_click",
        "ai_chat_business_catgory_selected", "ai_chat_caption_catgory_selected", "ai_chat_delete_click", "ai_chat_fun_catgory_selected", "ai_chat_generate_now_btn_click",
        "ai_chat_generate_watchad", "ai_chat_generate_xp", "ai_Chat_generated_successfully", "ai_chat_love_catgory_selected", "ai_chat_response_received",
        "ai_chat_social_catgory_selected", "ai_chat_suggestions_used", "ai_chat_used_chat_screen", "ai_chat_used_share_screen", "ai_chat_wallpaperai_catgory_selected",
        "ai_chat_work_catgory_selected", "ai_chat_writing_catgory_selected", "ai_common_category_selected", "ai_common_generated_successfully", "ai_counter1_ad_failed_to_show",
        "ai_counter2_ad_failed_to_show", "ai_creator_btn_click", "ai_custom_generated_successfully", "ai_download_btn_click", "ai_facebook_share_btn",
        "ai_fashionai_category_selected", "ai_fashionai_generated_successfully", "ai_festival_clicked", "ai_festival_download_click", "ai_festival_generate_watchad",
        "ai_festival_generate_xp", "ai_festival_remove_watermark_clicked", "ai_festival_retry_btn_click", "ai_festival_retry_popup_open", "ai_festival_share_clicked",
        "ai_festival_template_continue_click", "ai_festival_template_edit_click", "ai_festival_yml_template_clicked", "ai_generated_successfully", "ai_image_btn_click",
        "ai_image_firstscreen_next", "ai_image_firstscreen_skip", "ai_image_generate_now_btn_click", "ai_image_generate_watchad", "ai_image_generate_xp",
        "ai_image_generated_successfully", "ai_image_jpg_buypro_clicked", "ai_image_jpg_pro_ad_watched", "ai_image_pdf_buypro_clicked", "ai_image_pdf_pro_ad_watched",
        "ai_image_preview_screen_open", "ai_image_regenerate_btn_click", "ai_image_save", "ai_image_save_jpg_high", "ai_image_save_jpg_low",
        "ai_image_save_jpg_medium", "ai_image_save_jpg_pro_open", "ai_image_save_pdf", "ai_image_save_pdf_pro_open", "ai_image_secondscreen_next",
        "ai_image_secondscreen_skip", "ai_image_selected_share_screen", "ai_image_share_screen_open", "ai_image_thirdscreen_startclick", "ai_image_trynow_clicked",
        "ai_instagram_share_btn", "ai_interiorai_category_selected", "ai_interiorai_generated_successfully", "ai_invitation_clicked", "ai_invitation_download_click",
        "ai_invitation_generate_watchad", "ai_invitation_generate_xp", "ai_invitation_remove_watermark_clicked", "ai_invitation_retry_btn_click", "ai_invitation_retry_popup_open",
        "ai_invitation_share_clicked", "ai_invitation_template_continue_click", "ai_invitation_template_edit_click", "ai_invitation_yml_template_clicked", "ai_jewelleryai_category_selected",
        "ai_jewelleryai_generated_successfully", "ai_jewelleryaÄ±_generated_successfully", "ai_logo_category_selected", "ai_logo_generated_successfully", "ai_logo_subcategory_selected",
        "ai_logoai_category_selected", "ai_logoai_generated_successfully", "ai_love_category_selected", "ai_main_screen_skip_btn_click", "ai_normal_festival_template_edit_click",
        "ai_normal_invitation_template_edit_click", "ai_others_category_selected", "ai_others_generated_successfully", "ai_poster_clicked", "ai_poster_download_click",
        "ai_poster_edit_btn_click", "ai_poster_generate_watchad", "ai_poster_generate_xp", "ai_poster_remove_watermark_clicked", "ai_poster_retry_btn_click",
        "ai_poster_retry_popup_open", "ai_poster_share_clicked", "ai_poster_templete_continue_click", "ai_poster_yml_template_clicked", "ai_ratio_selected_16_9",
        "ai_ratio_selected_1_1", "ai_ratio_selected_9_16", "ai_ratio_selected_portrait", "ai_ratio_selected_square", "ai_regenerate_btn_click", "ai_remove_watermark_ad_watched",
        "ai_remove_watermark_one_time_btn_clicked", "ai_remove_watermark_pro_clicked", "ai_remove_watermark_pro_purchase_success", "ai_retry_btn_click", "ai_seemore_suggestion_item_click",
        "ai_share_btn_click", "ai_shared_with_other_source", "ai_skip_from_style", "ai_skip_from_subcategory", "ai_sticker_category_selected", "ai_sticker_generated_successfully",
        "ai_surpriseme_prompt_avatarai_clicked", "ai_surpriseme_prompt_barberai_clicked", "ai_surpriseme_prompt_common_clicked", "ai_surpriseme_prompt_fashionai_clicked",
        "ai_surpriseme_prompt_interiorai_clicked", "ai_surpriseme_prompt_jewelleryai_clicked", "ai_surpriseme_prompt_logoai_clicked", "ai_surpriseme_prompt_wallpaperai_clicked",
        "ai_total_api_calls", "ai_wallpaper_category_selected", "ai_wallpaper_generated_successfully", "ai_wallpaperai_category_selected", "ai_wallpaperai_generated_successfully",
        "ai_wallpaperaÄ±_generated_successfully", "ai_wallpapper_category_selected", "ai_whatsapp_share_btn", "ai_work_category_selected", "align_btn",
        "alphabetic_element_btn", "alphabetic_element_used", "ambedkarjayanti_element_btn", "ambedkarjayanti_element_used", "animals_birds_bg_clicked",
        "animals_birds_bg_used", "animals_element_btn", "animals_element_used", "api_ad_click_count_fail", "api_ad_list_fail", "api_ai_chat_deduct_xp_fail",
        "api_ai_chat_edit_text_fail", "api_ai_chat_history_fail", "api_ai_generate_img_fail", "api_ai_img_data_fail", "api_ai_img_deduct_xp_fail",
        "api_ai_img_fail", "api_ai_poster_deduct_xp_fail", "api_bg_category_fail", "api_bg_gradient_color_fail", "api_bg_img_fail", "api_bg_list_fail",
        "api_bg_search_fail", "api_call_dashboard_content", "api_call_seeall_clicked", "api_category_data_fail", "api_collect_referral_fail", "api_config_fail",
        "api_create_new_fail", "api_daily_pick_logo_fail", "api_daily_pick_you_may_like_fail", "api_data_loaded_dashboard_content", "api_data_loaded_main_category_dashboard",
        "api_data_loaded_seeall_clicked", "api_download_zip_fail", "api_edit_name_fail", "api_effect_fail", "api_festival_fail", "api_flyer_fail",
        "api_font_fail", "api_generate_ai_text_fail", "api_help_fail", "api_icon_category_fail", "api_icon_list_fail", "api_invitation_fail",
        "api_login_fail", "api_logo_fail", "api_main_category_list_fail", "api_response_error_bg_img_list", "api_response_error_category_data", "api_response_error_category_menu_list",
        "API_response_error_categoryList_content", "api_response_error_config", "API_response_error_config_content", "api_response_error_createnew_list", "API_response_error_createnewList_content",
        "api_response_error_dashboard_content", "api_response_error_effect_list", "api_response_error_festival_list", "api_response_error_flyer_list", "api_response_error_font_list",
        "API_response_error_fonts_content", "api_response_error_gradient_list", "api_response_error_invitation_list", "api_response_error_login_content", "api_response_error_logo_list",
        "API_response_error_search_list_content", "api_response_error_search_result_list", "api_response_error_search_screen_list", "api_response_error_socialmedia_list",
        "api_response_error_trending_list", "api_response_error_update_xp", "api_response_error_visiting_list", "api_response_error_youtube_list", "api_search_data_fail",
        "api_search_result_fail", "api_seen_template_fail", "api_show_referrer_fail", "api_social_media_fail", "api_subscription_data_fail", "api_subscription_verify_data_fail",
        "api_trending_fail", "api_update_xp_fail", "api_visiting_fail", "api_xp_purchase_fail", "api_you_may_like_fail", "api_youtube_link_fail",
        "app_launch", "app_remove", "app_store_refund", "app_store_subscription_cancel", "app_store_subscription_renew", "app_update",
        "aprilfool_element_btn", "aprilfool_element_used", "arrow_element_btn", "arrow_element_used", "art_element_btn",
        "art_element_used", "autofill_btn", "automobile_bg_clicked", "automobile_bg_used", "back_to_lobby",
        "back_to_lobby_yes_btn", "banner_ad_backup_loaded", "banner_ad_backup_loading_failed", "banner_ad_loaded", "banner_ad_loading_failed",
        "banner_astrozop_clicked", "banner_criczop_clicked", "banner_gamezop_clicked", "banner_newszop_clicked", "banner_quizzop_clicked",
        "barbie_element_btn", "barbie_element_used", "beaches_bg_clicked", "beaches_bg_used", "bg_btn",
        "bg_choosecolor_btn", "bg_gradiant_btn", "bg_import_btn", "bg_pickcolor_btn", "bg_removal_pro_ad_watched",
        "bg_remove_btn", "bg_remove_pro_open", "bg_reset_btn", "bg_solid_btn", "bg_stock_img_ad_watched",
        "bg_stock_img_click", "bg_stock_img_pro_open", "bgremoval_bg_buypro_clicked", "birthday_bg_clicked", "birthday_bg_used",
        "birthday_element_btn",
        "birthday_element_used", "boho_element_btn", "bookday_element_btn", "bookday_element_used", "border_buypro_click",
        "border_click", "border_dash_used", "border_dotes_used", "border_line_used", "border_pro_ad_watched",
        "border_pro_open", "border_text_share_clicked", "brush_element_btn", "brush_element_used", "bubbleshapefont_element_btn",
        "bubbleshapefont_element_used", "business_bg_clicked", "business_bg_used", "business_element_btn", "business_element_used",
        "callout_element_btn", "callout_element_used", "cancel_clicked_mysubscription", "cartoon_element_btn", "cartoon_element_used",
        "category_banner_astrozop_clicked", "category_banner_criczop_clicked", "category_banner_gamezop_clicked", "category_banner_newszop_clicked", "category_banner_quizzop_clicked",
        "check_google_response_not_purchased", "check_google_response_purchased", "choose_color_btn", "christmas_element_btn", "christmas_element_used",
        "circle_element_btn", "circle_element_used", "click_purchase_xp_loogy_xp_pack_01", "click_purchase_xp_loogy_xp_pack_02", "click_purchase_xp_loogy_xp_pack_03",
        "click_purchase_xp_loogy_xp_pack_04", "cloud_element_btn", "cloud_element_used", "cnw_3dlogos_save", "cnw_3dlogos_save_jpg",
        "cnw_advertising_save", "cnw_advertising_save_jpg", "cnw_alphabetic_save", "cnw_alphabetic_save_jpg", "cnw_alphabetic_save_png",
        "cnw_anniversary_save", "cnw_anniversary_save_jpg", "cnw_automobile_save", "cnw_automobile_save_jpg", "cnw_awardceremony_save",
        "cnw_awardceremony_save_jpg", "cnw_babyshower_save", "cnw_babyshower_save_jpg", "cnw_bhaidooj_save", "cnw_bhaidooj_save_jpg",
        "cnw_birthday_save", "cnw_birthday_save_jpg", "cnw_birthday_save_pdf", "cnw_bowlingparty_save", "cnw_bowlingparty_save_jpg",
        "cnw_btn_click", "cnw_business_save", "cnw_business_save_jpg", "cnw_business_save_pdf", "cnw_business_save_png",
        "cnw_businesswebinar_save", "cnw_businesswebinar_save_jpg", "cnw_camping_save", "cnw_camping_save_jpg", "cnw_carnival_save",
        "cnw_carnival_save_jpg", "cnw_charityandfundraisers_save", "cnw_charityandfundraisers_save_jpg", "cnw_christmas_save", "cnw_christmas_save_jpg",
        "cnw_clubparty_save", "cnw_clubparty_save_jpg", "cnw_colorful_save", "cnw_colorful_save_jpg", "cnw_communication_save",
        "cnw_communication_save_jpg", "cnw_competition_save", "cnw_competition_save_jpg", "cnw_contest_save", "cnw_contest_save_jpg",
        "cnw_corporate_save", "cnw_corporate_save_jpg", "cnw_corporate_save_png", "cnw_cradleceremony_save", "cnw_cradleceremony_save_jpg",
        "cnw_cradleceremony_save_pdf", "cnw_cricket_save", "cnw_cricket_save_jpg", "cnw_diwali_save", "cnw_diwali_save_jpg",
        "cnw_doodle_save", "cnw_doodle_save_jpg", "cnw_durgapooja_save", "cnw_durgapooja_save_jpg", "cnw_dussehra_save",
        "cnw_dussehra_save_jpg", "cnw_earthday_save", "cnw_earthday_save_jpg", "cnw_education_save", "cnw_education_save_jpg",
        "cnw_education_save_pdf", "cnw_education_save_png", "cnw_educational_save", "cnw_educational_save_jpg", "cnw_entertainment_save", "cnw_entertainment_save_jpg",
        "cnw_entertainmnet_save", "cnw_entertainmnet_save_jpg", "cnw_esports_save", "cnw_esports_save_jpg", "cnw_eventplanner_save",
        "cnw_eventplanner_save_jpg", "cnw_events_save", "cnw_events_save_jpg", "cnw_facebookcovers", "cnw_facebookcovers_save",
        "cnw_facebookcovers_save_jpg", "cnw_facebookcovers_save_png", "cnw_facebookpost", "cnw_facebookpost_save", "cnw_facebookpost_save_jpg",
        "cnw_facebookpost_save_pdf", "cnw_farewell_save", "cnw_farewell_save_jpg", "cnw_fashion_save", "cnw_fashion_save_jpg",
        "cnw_fbpost", "cnw_feedback_editleave_open", "cnw_feedback_editleave_submit", "cnw_feedback_postediting_open", "cnw_feedback_postediting_submit",
        "cnw_festivalcard_save", "cnw_festivalcard_save_jpg", "cnw_festivalcard_save_pdf", "cnw_festivalcard_save_png", "cnw_fintech_save",
        "cnw_fintech_save_jpg", "cnw_fintech_save_png", "cnw_fitness_save", "cnw_fitness_save_jpg", "cnw_fl",
        "cnw_fl_exit_no_clicked", "cnw_fl_exit_popup_open", "cnw_fl_exit_savedraft_clicked", "cnw_fl_exit_yes_clicked", "cnw_flyers_save",
        "cnw_flyers_save_jpg", "cnw_flyers_save_pdf", "cnw_flyers_save_png", "cnw_food_save", "cnw_food_save_jpg",
        "cnw_foodparty_save", "cnw_foodparty_save_jpg", "cnw_friendshipday_save", "cnw_friendshipday_save_jpg", "cnw_ft",
        "cnw_ft_exit_no_clicked", "cnw_ft_exit_popup_open", "cnw_ft_exit_savedraft_clicked", "cnw_ft_exit_yes_clicked", "cnw_funeral_save",
        "cnw_funeral_save_jpg", "cnw_game_save", "cnw_game_save_jpg", "cnw_ganeshchaturthi_save", "cnw_ganeshchaturthi_save_jpg",
        "cnw_gettogether_save", "cnw_gettogether_save_jpg", "cnw_gettogether_save_pdf", "cnw_grandopening_save", "cnw_grandopening_save_jpg",
        "cnw_grandopening_save_pdf", "cnw_gurupurnima_save", "cnw_gurupurnima_save_jpg", "cnw_haldiceremony_save", "cnw_haldiceremony_save_jpg",
        "cnw_handwriting_save", "cnw_handwriting_save_jpg", "cnw_handwriting_save_pdf", "cnw_handwriting_save_png", "cnw_health_save",
        "cnw_health_save_jpg", "cnw_heart_save", "cnw_heart_save_jpg", "cnw_hiring_save", "cnw_hiring_save_jpg",
        "cnw_holi_save", "cnw_holi_save_jpg", "cnw_holidayparty_save", "cnw_holidayparty_save_jpg", "cnw_homeservice_save",
        "cnw_homeservice_save_jpg", "cnw_housewarming_save", "cnw_housewarming_save_jpg", "cnw_housewarming_save_pdf", "cnw_housewarming_save_png",
        "cnw_ic", "cnw_ic_exit_no_clicked", "cnw_ic_exit_popup_open", "cnw_ic_exit_savedraft_clicked", "cnw_ic_exit_yes_clicked",
        "cnw_inaugurations_save", "cnw_inaugurations_save_jpg", "cnw_independenceday_save", "cnw_independenceday_save_jpg", "cnw_instagrampost",
        "cnw_instagrampost_save", "cnw_instagrampost_save_jpg", "cnw_instagrampost_save_pdf", "cnw_instagrampost_save_png", "cnw_instagramstory",
        "cnw_instagramstory_save", "cnw_instagramstory_save_jpg", "cnw_instagramstory_save_pdf", "cnw_instagramstory_save_png", "cnw_invitationcards_save",
        "cnw_invitationcards_save_jpg", "cnw_invitationcards_save_pdf", "cnw_invitationcards_save_png", "cnw_janmashtami_save", "cnw_janmashtami_save_jpg",
        "cnw_jewellery_save", "cnw_jewellery_save_jpg", "cnw_karwachauth_save", "cnw_karwachauth_save_jpg", "cnw_kittyparty_save",
        "cnw_kittyparty_save_jpg", "cnw_laborday_save", "cnw_laborday_save_jpg", "cnw_lg", "cnw_lg_exit_no_clicked",
        "cnw_lg_exit_popup_open", "cnw_lg_exit_savedraft_clicked", "cnw_lg_exit_yes_clicked", "cnw_lg_save",
        "cnw_lg_save_jpg", "cnw_lifestyle_save", "cnw_lifestyle_save_jpg", "cnw_linkedinpost", "cnw_linkedinpost_save",
        "cnw_linkedinpost_save_jpg", "cnw_linkedinpost_save_png", "cnw_logos_save", "cnw_logos_save_jpg", "cnw_logos_save_pdf",
        "cnw_logos_save_png", "cnw_mahashivratri_save", "cnw_mahashivratri_save_jpg", "cnw_makarsankranti_save", "cnw_makarsankranti_save_jpg",
        "cnw_makeup_save", "cnw_makeup_save_jpg", "cnw_medical_save", "cnw_medical_save_jpg", "cnw_mehndiceremony_save",
        "cnw_mehndiceremony_save_jpg", "cnw_movienightparty_save", "cnw_movienightparty_save_jpg", "cnw_muharram_save", "cnw_muharram_save_jpg",
        "cnw_mundanceremony_save", "cnw_mundanceremony_save_jpg", "cnw_music_save", "cnw_music_save_jpg", "cnw_namingceremony_save",
        "cnw_namingceremony_save_jpg", "cnw_namingceremony_save_pdf", "cnw_navratri_save", "cnw_navratri_save_jpg",
        "cnw_openhouseparty_save", "cnw_openhouseparty_save_jpg", "cnw_photocollage", "cnw_photocollage_save", "cnw_photocollage_save_jpg",
        "cnw_photocollage_save_pdf", "cnw_photocollage_save_png", "cnw_photography_save", "cnw_photography_save_jpg", "cnw_picnic_save",
        "cnw_picnic_save_jpg", "cnw_pooja_save", "cnw_pooja_save_jpg", "cnw_princessparty_save", "cnw_princessparty_save_jpg",
        "cnw_productbranding_save", "cnw_productbranding_save_jpg", "cnw_quotes_save", "cnw_quotes_save_jpg", "cnw_rakshabandhan_save",
        "cnw_rakshabandhan_save_jpg",
        "cnw_realestate_save", "cnw_realestate_save_jpg", "cnw_reception_save", "cnw_reception_save_jpg", "cnw_religious_save",
        "cnw_religious_save_jpg", "cnw_religiousparty_save", "cnw_religiousparty_save_jpg", "cnw_ringceremony_save", "cnw_ringceremony_save_jpg",
        "cnw_rounded_save", "cnw_rounded_save_jpg", "cnw_sale_save", "cnw_sale_save_jpg", "cnw_savethedate_save", "cnw_savethedate_save_jpg",
        "cnw_seminar_save", "cnw_seminar_save_jpg", "cnw_shravanmaas_save", "cnw_shravanmaas_save_jpg", "cnw_sleepover_save",
        "cnw_sleepover_save_jpg", "cnw_sm_exit_no_clicked", "cnw_sm_exit_popup_open", "cnw_sm_exit_savedraft_clicked", "cnw_sm_exit_yes_clicked",
        "cnw_social_save", "cnw_social_save_jpg", "cnw_spring_save", "cnw_spring_save_jpg", "cnw_st", "cnw_st_exit_no_clicked",
        "cnw_st_exit_popup_open", "cnw_st_exit_savedraft_clicked", "cnw_st_exit_yes_clicked", "cnw_sweetsixteen_save", "cnw_sweetsixteen_save_jpg",
        "cnw_teachersday_save", "cnw_teachersday_save_jpg", "cnw_teaparty_save", "cnw_teaparty_save_jpg", "cnw_technology_save",
        "cnw_technology_save_jpg", "cnw_textile_save", "cnw_textile_save_jpg", "cnw_travel_save", "cnw_travel_save_jpg", "cnw_travel_save_pdf",
        "cnw_vaghbaras_save", "cnw_vaghbaras_save_jpg", "cnw_vc", "cnw_vc_exit_no_clicked", "cnw_vc_exit_popup_open", "cnw_vc_exit_savedraft_clicked",
        "cnw_vc_exit_yes_clicked", "cnw_vintage_save", "cnw_vintage_save_jpg", "cnw_visitingcards_save", "cnw_visitingcards_save_jpg",
        "cnw_visitingcards_save_pdf", "cnw_visitingcards_save_png", "cnw_wedding_save", "cnw_wedding_save_jpg", "cnw_whatsappstatus",
        "cnw_whatsappstatus_save", "cnw_whatsappstatus_save_jpg", "cnw_whatsappstatus_save_pdf", "cnw_whatsappstatus_save_png", "cnw_yogaday_save",
        "cnw_yogaday_save_jpg", "cnw_youthday_save", "cnw_youthday_save_jpg", "cnw_youtubebanner", "cnw_youtubebanner_save",
        "cnw_youtubebanner_save_jpg", "cnw_youtubebanner_save_pdf", "cnw_youtubebanner_save_png", "cnw_youtubethumbnails", "cnw_youtubethumbnails_save",
        "cnw_youtubethumbnails_save_jpg", "cnw_youtubethumbnails_save_pdf", "cnw_youtubethumbnails_save_png", "color_button", "creative_element_btn",
        "creative_element_used", "cricket_element_btn", "cricket_element_used", "curvtext_buypro_click", "curvtext_click", "curvtext_pro_open",
        "cyberpunk_element_btn", "cyberpunk_element_used", "daily_bonus_day1_reward_collect", "daily_bonus_day2_reward_collect", "daily_bonus_day3_reward_collect",
        "daily_bonus_open_homescreen", "daily_bonus_open_taskcenter", "day_1_user_no_draft_content", "day_1_user_no_saved_content", "diwali_element_btn",
        "diwali_element_used", "dont_losseoffer_popup_close", "dont_losseoffer_popup_open", "dont_losseoffer_subscribe_btn_click", "doodle_element_btn",
        "doodle_element_used", "download_btn_click", "download_fail_error", "download_fail_error_in_error_section", "dp__content_edit_clicked",
        "dp_btn_click", "dp_content_buypro_clicked", "dp_content_change", "dp_content_pro_ad_watched", "dp_cricket_content_clicked",
        "dp_cricket_content_edit_clicked", "dp_cricket_content_save_clicked", "dp_cricket_save", "dp_cricket_seemore", "dp_details_popup_open",
        "dp_details_saved", "dp_devotional_content_clicked", "dp_devotional_content_edit_clicked", "dp_devotional_content_save_clicked", "dp_devotional_save",
        "dp_devotional_seemore", "dp_festival_content_clicked", "dp_festival_content_edit_clicked", "dp_festival_content_save_clicked", "dp_festival_save",
        "dp_festival_seemore", "dp_frame_change", "dp_friendshipday_content_clicked", "dp_friendshipday_content_edit_clicked", "dp_friendshipday_content_save_clicked",
        "dp_friendshipday_seemore", "dp_goodmorning_content_clicked", "dp_goodmorning_content_edit_clicked", "dp_goodmorning_content_save_clicked",
        "dp_goodmorning_save", "dp_goodmorning_seemore", "dp_goodthoughts_content_clicked", "dp_goodthoughts_content_edit_clicked", "dp_goodthoughts_content_save_clicked",
        "dp_goodthoughts_save", "dp_goodthoughts_seemore", "dp_independenceday_content_clicked", "dp_independenceday_content_edit_clicked", "dp_independenceday_content_save_clicked",
        "dp_independenceday_save", "dp_independenceday_seemore", "dp_janmashtami_content_clicked", "dp_janmashtami_content_edit_clicked", "dp_janmashtami_content_save_clicked",
        "dp_janmashtami_save", "dp_janmashtami_seemore", "dp_jpg_buypro_clicked", "dp_jpg_high_save", "dp_jpg_low_save", "dp_jpg_medium_save", "dp_jpg_pro_ad_watched",
        "dp_leadersquotes_content_clicked", "dp_leadersquotes_content_edit_clicked", "dp_leadersquotes_content_save_clicked", "dp_leadersquotes_save", "dp_leadersquotes_seemore",
        "dp_nagpanchami_content_clicked", "dp_nagpanchami_content_edit_clicked", "dp_nagpanchami_content_save_clicked", "dp_nagpanchami_save", "dp_nagpanchami_seemore",
        "dp_no_details_entered", "dp_olympic2024_content_clicked", "dp_olympic2024_content_edit_clicked", "dp_olympic2024_content_save_clicked", "dp_olympic2024_save",
        "dp_olympic2024_seemore", "dp_pdf_buypro_clicked", "dp_pdf_high_save", "dp_pdf_pro_ad_watched", "dp_pro_ad_watched", "dp_pro_buypro_clicked",
        "dp_pro_open", "dp_pro_watchad", "dp_rakshabandhan_content_clicked", "dp_rakshabandhan_content_edit_clicked", "dp_rakshabandhan_content_save_clicked",
        "dp_rakshabandhan_save", "dp_rakshabandhan_seemore", "dp_remove_watermark_ad_watched", "dp_remove_watermark_btn_click", "dp_remove_watermark_continue_clicked",
        "dp_remove_watermark_one_time_btn_clicked", "dp_remove_watermark_popup_open", "dp_remove_watermark_pro_clicked", "dp_remove_watermark_screen_open", "dp_remove_watermark_watch_video_clicked",
        "dp_save_jpg_pro_open", "dp_save_pdf_pro_open", "dp_shravanmass_content_clicked", "dp_shravanmass_content_edit_clicked", "dp_shravanmass_content_save_clicked",
        "dp_shravanmass_save", "dp_shravanmass_seemore", "dp_total_jpg_save", "dp_total_pdf_save", "draft_btn_click", "durgapooja_element_btn",
        "durgapooja_element_used", "dussehra_element_btn", "dussehra_element_used", "earthday_element_btn", "earthday_element_used", "easterday_element_btn",
        "editing_ai_chat_click", "editing_ai_chat_continuewrite", "editing_ai_chat_customtext", "editing_ai_chat_formal", "editing_ai_chat_improve",
        "editing_ai_chat_shorten", "editing_ai_image_click", "editing_ai_image_import", "editing_total_ai_chat_used", "editing_total_ai_image_used",
        "editor_screen_open", "education_element_btn", "education_element_used", "effect_btn", "effects_apply", "effects_pro_ad_watched",
        "effects_pro_buypro_clicked", "effects_pro_open", "element_btn", "element_buypro_clicked", "element_content_count", "element_next_btn_click",
        "element_pro_ad_watched", "element_pro_open", "emoji_element_btn", "emoji_element_used", "environmental_element_btn", "environmental_element_used",
        "events_btn_click", "exit_popup_no_click", "exit_popup_open", "exit_popup_yes_click", "fabric_bg_clicked", "fabric_bg_used",
        "facebook_share_btn", "facebookcovers_bg_clicked", "facebookcovers_bg_used", "facebookpost_bg_clicked", "facebookpost_bg_used",
        "feather_element_btn", "feather_element_used", "feedback_appleave_close_without_submit", "feedback_appleave_open", "feedback_appleave_submit",
        "feedback_editleave_close_without_submit", "feedback_editleave_open", "feedback_editleave_submit", "feedback_postediting_open", "feedback_postediting_submit",
        "festival_element_btn", "festival_element_used", "festivalcards_bg_clicked", "festivalcards_bg_used", "first_open", "fitness_element_btn",
        "fitness_element_used", "fl__save", "fl__save_jpg", "fl_aifestival", "fl_aifestival_save", "fl_aifestival_save_jpg", "fl_aifestival_save_pdf",
        "fl_bikeevent", "fl_bikeevent_edit_btn_click", "fl_bikeevent_save", "fl_bikeevent_save_jpg", "fl_bikeevent_seemore", "fl_birthday",
        "fl_birthday_edit_btn_click", "fl_birthday_save", "fl_birthday_save_jpg", "fl_birthday_save_pdf", "fl_birthday_save_png", "fl_birthday_seemore",
        "fl_btn_click", "fl_business", "fl_business_edit_btn_click", "fl_business_save", "fl_business_save_jpg", "fl_business_save_pdf",
        "fl_business_save_png", "fl_business_seemore", "fl_camping", "fl_camping_edit_btn_click", "fl_camping_save", "fl_camping_save_jpg",
        "fl_camping_save_pdf", "fl_camping_save_png", "fl_camping_seemore", "fl_childrensday", "fl_contest",
        "fl_contest_edit_btn_click", "fl_contest_save", "fl_contest_save_jpg", "fl_contest_seemore", "fl_cricket",
        "fl_cricket_edit_btn_click", "fl_cricket_save", "fl_cricket_save_jpg", "fl_cricket_seemore", "fl_durgapooja",
        "fl_educational", "fl_educational_edit_btn_click", "fl_educational_save", "fl_educational_save_jpg", "fl_educational_seemore",
        "fl_entertainment", "fl_entertainment_edit_btn_click", "fl_entertainment_save", "fl_entertainment_save_jpg", "fl_entertainment_save_pdf",
        "fl_entertainment_seemore", "fl_exit_no_clicked", "fl_exit_popup_open", "fl_exit_savedraft_clicked", "fl_exit_yes_clicked",
        "fl_fitness", "fl_fitness_edit_btn_click", "fl_fitness_save", "fl_fitness_save_jpg", "fl_fitness_save_pdf",
        "fl_fitness_save_png", "fl_fitness_seemore", "fl_flyers_save", "fl_flyers_save_jpg", "fl_flyers_save_pdf",
        "fl_flyers_save_png", "fl_food_drink", "fl_food_drink_edit_btn_click", "fl_football", "fl_football_edit_btn_click",
        "fl_football_save", "fl_football_save_jpg", "fl_football_save_pdf", "fl_football_save_png", "fl_football_seemore",
        "fl_gettogether", "fl_gettogether_edit_btn_click", "fl_gettogether_save", "fl_gettogether_save_jpg", "fl_gettogether_save_pdf",
        "fl_gettogether_seemore", "fl_hiring", "fl_hiring_edit_btn_click", "fl_hiring_save", "fl_hiring_save_jpg",
        "fl_hiring_seemore", "fl_inaugurations", "fl_inaugurations_edit_btn_click", "fl_inaugurations_save", "fl_inaugurations_save_jpg",
        "fl_inaugurations_save_pdf", "fl_inaugurations_seemore", "fl_lifestyle", "fl_lifestyle_edit_btn_click", "fl_lifestyle_save",
        "fl_lifestyle_save_jpg", "fl_lifestyle_seemore", "fl_newyearparty", "fl_newyearparty_edit_btn_click", "fl_newyearparty_save",
        "fl_newyearparty_save_jpg", "fl_newyearparty_seemore", "fl_onam", "fl_onam_save", "fl_onam_save_jpg", "fl_patricksday",
        "fl_pooja", "fl_princessparty", "fl_princessparty_save", "fl_princessparty_save_jpg", "fl_pro_buypro_clicked",
        "fl_pro_open", "fl_pro_watchad", "fl_productbranding", "fl_productbranding_edit_btn_click", "fl_productbranding_save",
        "fl_productbranding_save_jpg", "fl_productbranding_save_pdf", "fl_productbranding_seemore", "fl_realestate",
        "fl_realestate_edit_btn_click", "fl_realestate_save", "fl_realestate_save_jpg", "fl_realestate_seemore", "fl_sale",
        "fl_sale_edit_btn_click", "fl_sale_save", "fl_sale_save_jpg", "fl_sale_save_pdf", "fl_sale_save_png",
        "fl_sale_seemore", "fl_salon", "fl_salon_edit_btn_click", "fl_salon_save", "fl_salon_save_jpg", "fl_salon_seemore",
        "fl_seminar", "fl_seminar_edit_btn_click", "fl_seminar_save", "fl_seminar_save_jpg", "fl_seminar_seemore",
        "fl_social", "fl_social_edit_btn_click", "fl_social_save", "fl_social_save_jpg", "fl_social_save_pdf",
        "fl_social_save_png", "fl_social_seemore", "fl_thanksgiving", "fl_thanksgiving_edit_btn_click", "fl_thanksgiving_save",
        "fl_thanksgiving_save_jpg", "fl_thanksgiving_seemore", "fl_travel", "fl_travel_edit_btn_click", "fl_travel_save",
        "fl_travel_save_jpg", "fl_travel_seemore", "fl_yogaday", "fl_yogaday_save", "fl_yogaday_save_jpg", "flag_element_btn",
        "flag_element_used", "floral_element_btn", "floral_element_used", "flyers_bg_clicked", "flyers_bg_used",
        "font_btn", "font_buypro_clicked", "font_pro_ad_watched", "font_pro_open", "football_element_btn",
        "football_element_used", "frame_image_jpg_buypro_clicked", "frame_image_jpg_pro_ad_watched", "frame_image_pdf_buypro_clicked",
        "frame_image_pdf_pro_ad_watched", "frame_image_save_jpg_pro_open", "frame_image_save_pdf_pro_open", "frame_pro_ad_watched",
        "frame_remove_watermark_ad_watched", "frame_remove_watermark_popup_open", "frame_remove_watermark_pro_clicked", "frames_element_btn",
        "frames_element_used", "friendshipday_element_btn", "friendshipday_element_used", "ft__save", "ft__save_jpg",
        "ft__save_pdf", "ft_aprilfoolday", "ft_aprilfoolday_edit_btn_click", "ft_babasahebambedkarjayanti", "ft_babasahebambedkarjayanti_save",
        "ft_babasahebambedkarjayanti_save_jpg", "ft_bhaidooj", "ft_bhaidooj_edit_btn_click", "ft_bhaidooj_save", "ft_bhaidooj_save_jpg",
        "ft_bhaidooj_seemore", "ft_btn_click", "ft_childrensday", "ft_childrensday_edit_btn_click", "ft_childrensday_save",
        "ft_childrensday_save_jpg", "ft_childrensday_seemore", "ft_christmas", "ft_christmas_edit_btn_click", "ft_christmas_save",
        "ft_christmas_save_jpg", "ft_christmas_seemore", "ft_columbusday", "ft_columbusday_edit_btn_click", "ft_columbusday_seemore",
        "ft_diwali", "ft_diwali_edit_btn_click", "ft_diwali_save", "ft_diwali_save_jpg", "ft_diwali_seemore", "ft_durgapooja",
        "ft_durgapooja_edit_btn_click", "ft_durgapooja_save", "ft_durgapooja_save_jpg", "ft_durgapooja_seemore", "ft_dussehra",
        "ft_dussehra_edit_btn_click", "ft_dussehra_save", "ft_dussehra_save_jpg", "ft_dussehra_seemore", "ft_earthday",
        "ft_earthday_edit_btn_click", "ft_earthday_save", "ft_earthday_save_jpg", "ft_earthday_seemore", "ft_easterday",
        "ft_easterday_edit_btn_click", "ft_electionsday", "ft_electionsday_edit_btn_click", "ft_electionsday_save", "ft_electionsday_save_jpg",
        "ft_electionsday_seemore", "ft_entertainment", "ft_entertainment_save", "ft_entertainment_save_jpg", "ft_environmentday",
        "ft_environmentday_edit_btn_click", "ft_environmentday_save", "ft_environmentday_save_jpg", "ft_environmentday_seemore",
        "ft_exit_no_clicked", "ft_exit_popup_open", "ft_exit_savedraft_clicked", "ft_exit_yes_clicked", "ft_festivalcard_save",
        "ft_festivalcard_save_jpg", "ft_festivalcard_save_png", "ft_friendshipday", "ft_friendshipday_edit_btn_click", "ft_friendshipday_save",
        "ft_friendshipday_save_jpg", "ft_friendshipday_save_pdf", "ft_friendshipday_seemore", "ft_ganeshchaturthi", "ft_ganeshchaturthi_edit_btn_click",
        "ft_ganeshchaturthi_save", "ft_ganeshchaturthi_save_jpg", "ft_ganeshchaturthi_seemore", "ft_gettogether", "ft_gettogether_save",
        "ft_gettogether_save_jpg", "ft_gettogether_save_pdf", "ft_goodfriday", "ft_goodfriday_edit_btn_click", "ft_goodfriday_save",
        "ft_goodfriday_save_jpg", "ft_goodfriday_seemore", "ft_gudipadwa", "ft_gudipadwa_edit_btn_click", "ft_gudipadwa_save",
        "ft_gudipadwa_save_jpg", "ft_gudipadwa_seemore", "ft_gurunanakjayanti", "ft_gurunanakjayanti_edit_btn_click", "ft_gurunanakjayanti_save",
        "ft_gurunanakjayanti_save_jpg", "ft_gurunanakjayanti_seemore", "ft_gurupurnima", "ft_gurupurnima_edit_btn_click", "ft_gurupurnima_save",
        "ft_gurupurnima_save_jpg", "ft_gurupurnima_save_pdf", "ft_gurupurnima_save_png", "ft_gurupurnima_seemore", "ft_halloween",
        "ft_halloween_edit_btn_click", "ft_halloween_save", "ft_halloween_save_jpg", "ft_halloween_seemore", "ft_holi",
        "ft_holi_edit_btn_click", "ft_holi_save", "ft_holi_save_jpg", "ft_holi_seemore", "ft_independenceday",
        "ft_independenceday_edit_btn_click", "ft_independenceday_save", "ft_independenceday_save_jpg", "ft_independenceday_save_pdf",
        "ft_independenceday_save_png", "ft_independenceday_seemore", "ft_janmashtami", "ft_janmashtami_edit_btn_click",
        "ft_janmashtami_save", "ft_janmashtami_save_jpg", "ft_janmashtami_save_pdf", "ft_janmashtami_save_png", "ft_janmashtami_seemore",
        "ft_kalichaudas", "ft_kalichaudas_edit_btn_click", "ft_kalichaudas_save", "ft_kalichaudas_save_jpg", "ft_kalichaudas_seemore",
        "ft_karwachauth", "ft_karwachauth_edit_btn_click", "ft_karwachauth_save",
        "ft_karwachauth_save_jpg", "ft_karwachauth_seemore", "ft_labhpancham", "ft_labhpancham_edit_btn_click", "ft_labhpancham_save",
        "ft_labhpancham_save_jpg", "ft_labhpancham_save_pdf", "ft_labhpancham_seemore", "ft_laborday", "ft_laborday_edit_btn_click",
        "ft_laborday_seemore", "ft_lifestyle", "ft_lohri", "ft_lohri_edit_btn_click", "ft_lohri_save", "ft_lohri_save_jpg",
        "ft_mahashivratri", "ft_mahashivratri_edit_btn_click", "ft_mahashivratri_save", "ft_mahashivratri_save_jpg", "ft_mahashivratri_seemore",
        "ft_makarsankranti", "ft_makarsankranti_edit_btn_click", "ft_makarsankranti_save", "ft_makarsankranti_save_jpg", "ft_makarsankranti_seemore",
        "ft_memorialday", "ft_memorialday_edit_btn_click", "ft_memorialday_save", "ft_memorialday_save_jpg", "ft_memorialday_save_pdf",
        "ft_memorialday_seemore", "ft_micchamidukkadam", "ft_micchamidukkadam_edit_btn_click", "ft_micchamidukkadam_seemore", "ft_muharram",
        "ft_muharram_edit_btn_click", "ft_muharram_save", "ft_muharram_save_jpg", "ft_muharram_seemore", "ft_navratri",
        "ft_navratri_edit_btn_click", "ft_navratri_save", "ft_navratri_save_jpg", "ft_navratri_seemore", "ft_newyear",
        "ft_newyear_edit_btn_click", "ft_newyear_save", "ft_newyear_save_jpg", "ft_newyear_seemore", "ft_onam",
        "ft_onam_edit_btn_click", "ft_onam_save", "ft_onam_save_jpg", "ft_onam_seemore", "ft_patricksday",
        "ft_patricksday_edit_btn_click", "ft_pongal", "ft_pongal_edit_btn_click", "ft_pro_buypro_clicked", "ft_pro_open",
        "ft_pro_watchad", "ft_rakshabandhan", "ft_rakshabandhan_edit_btn_click", "ft_rakshabandhan_save", "ft_rakshabandhan_save_jpg",
        "ft_rakshabandhan_save_pdf", "ft_rakshabandhan_save_png", "ft_rakshabandhan_seemore", "ft_ramnavami", "ft_ramnavami_edit_btn_click",
        "ft_ramnavami_save", "ft_ramnavami_save_jpg", "ft_ramnavami_seemore", "ft_republicday", "ft_republicday_edit_btn_click",
        "ft_republicday_save", "ft_republicday_save_jpg", "ft_republicday_seemore", "ft_sharadpurnima", "ft_sharadpurnima_edit_btn_click",
        "ft_sharadpurnima_save", "ft_sharadpurnima_save_jpg", "ft_sharadpurnima_seemore", "ft_shravanmaas", "ft_shravanmaas_edit_btn_click",
        "ft_shravanmaas_save", "ft_shravanmaas_save_jpg", "ft_shravanmaas_save_pdf", "ft_shravanmaas_save_png", "ft_shravanmaas_seemore",
        "ft_shubhdhanteras", "ft_shubhdhanteras_edit_btn_click", "ft_shubhdhanteras_seemore", "ft_siblingsday", "ft_siblingsday_edit_btn_click",
        "ft_siblingsday_save", "ft_siblingsday_save_jpg", "ft_siblingsday_seemore", "ft_spring", "ft_spring_edit_btn_click",
        "ft_spring_seemore", "ft_teachersday", "ft_teachersday_edit_btn_click", "ft_teachersday_save", "ft_teachersday_save_jpg",
        "ft_teachersday_seemore", "ft_vaghbaras", "ft_vaghbaras_edit_btn_click", "ft_vaghbaras_save", "ft_vaghbaras_save_jpg",
        "ft_vaghbaras_seemore", "ft_valentinesday", "ft_valentinesday_edit_btn_click", "ft_valentinesday_save", "ft_valentinesday_save_jpg",
        "ft_valentinesday_seemore", "ft_vasantpanchami", "ft_vasantpanchami_edit_btn_click", "ft_vasantpanchami_save", "ft_vasantpanchami_save_jpg",
        "ft_vasantpanchami_seemore", "ft_veteransday", "ft_veteransday_edit_btn_click", "ft_veteransday_save", "ft_veteransday_save_jpg",
        "ft_veteransday_seemore", "ft_womensday", "ft_womensday_edit_btn_click", "ft_womensday_save", "ft_womensday_save_jpg",
        "ft_womensday_save_png", "ft_womensday_seemore", "ft_worldbookday", "ft_worldbookday_edit_btn_click", "ft_worldbookday_save",
        "ft_worldbookday_save_jpg", "ft_worldbookday_seemore", "ft_worldhealthday", "ft_worldhealthday_edit_btn_click", "ft_worldhealthday_save",
        "ft_worldhealthday_save_jpg", "ft_worldmusicday", "ft_worldmusicday_edit_btn_click", "ft_worldmusicday_save", "ft_worldmusicday_save_jpg",
        "ft_worldmusicday_seemore", "ft_yogaday", "ft_yogaday_edit_btn_click", "ft_yogaday_save", "ft_yogaday_save_jpg",
        "ft_yogaday_save_pdf", "ft_yogaday_seemore", "ft_youthday", "ft_youthday_edit_btn_click", "ft_youthday_save",
        "ft_youthday_save_jpg", "ft_youthday_seemore", "gamezop", "gandhijayanti_element_btn", "gandhijayanti_element_used",
        "ganeshchaturthi_element_btn", "ganeshchaturthi_element_used", "give_feedback_mysubscription", "goodfriday_element_btn",
        "goodfriday_element_used", "gradient_bg_btn", "gradient_bg_buypro_clicked", "gradient_bg_pro_ad_watched", "gradient_bg_pro_open",
        "grid_element_btn", "grid_element_used", "gudipadwa_element_btn", "gudipadwa_element_used", "halloween_element_btn",
        "halloween_element_used", "handcraft_element_btn", "handcraft_element_used", "healthday_element_btn", "healthday_element_used",
        "heart_element_btn", "heart_element_used", "help_btn", "holi_element_btn", "holi_element_used", "holographic_element_btn",
        "holographic_element_used", "home_btn_click", "how_to_use_btn", "ic__save", "ic__save_jpg", "ic__save_pdf",
        "ic__save_png", "ic_anniversary", "ic_anniversary_edit_btn_click", "ic_anniversary_save", "ic_anniversary_save_jpg",
        "ic_anniversary_save_pdf", "ic_anniversary_seemore", "ic_awardceremony", "ic_awardceremony_edit_btn_click", "ic_awardceremony_save",
        "ic_awardceremony_save_jpg", "ic_awardceremony_seemore", "ic_babyshower", "ic_babyshower_edit_btn_click", "ic_babyshower_save",
        "ic_babyshower_save_jpg", "ic_babyshower_save_pdf", "ic_babyshower_save_png", "ic_babyshower_seemore", "ic_bachelorparty",
        "ic_bachelorparty_edit_btn_click", "ic_bachelorparty_save", "ic_bachelorparty_save_jpg", "ic_bachelorparty_seemore",
        "ic_baptismandchristening_seemore", "ic_barorbatmitzvah", "ic_barorbatmitzvah_edit_btn_click", "ic_barorbatmitzvah_save",
        "ic_barorbatmitzvah_save_jpg", "ic_barorbatmitzvah_save_pdf", "ic_barorbatmitzvah_save_png", "ic_barorbatmitzvah_seemore",
        "ic_beachparty", "ic_beachparty_edit_btn_click", "ic_beachparty_save", "ic_beachparty_save_jpg", "ic_beachparty_seemore",
        "ic_birthday", "ic_birthday_edit_btn_click", "ic_birthday_save", "ic_birthday_save_jpg", "ic_birthday_save_pdf",
        "ic_birthday_save_png", "ic_birthday_seemore", "ic_bowlingparty", "ic_bowlingparty_edit_btn_click", "ic_bowlingparty_save",
        "ic_bowlingparty_save_jpg", "ic_bowlingparty_seemore", "ic_bridalshower", "ic_bridalshower_edit_btn_click", "ic_bridalshower_save",
        "ic_bridalshower_save_jpg", "ic_bridalshower_seemore", "ic_btn_click", "ic_businesswebinar", "ic_businesswebinar_edit_btn_click",
        "ic_businesswebinar_save", "ic_businesswebinar_save_jpg", "ic_businesswebinar_save_pdf", "ic_businesswebinar_seemore",
        "ic_carnival", "ic_carnival_edit_btn_click", "ic_carnival_save", "ic_carnival_save_jpg", "ic_carnival_save_pdf",
        "ic_carnival_seemore", "ic_charityandfundraisers", "ic_charityandfundraisers_edit_btn_click", "ic_charityandfundraisers_save",
        "ic_charityandfundraisers_save_jpg", "ic_charityandfundraisers_seemore", "ic_christmasparty", "ic_christmasparty_edit_btn_click",
        "ic_christmasparty_save", "ic_christmasparty_save_jpg", "ic_christmasparty_seemore", "ic_clubparty", "ic_clubparty_edit_btn_click",
        "ic_clubparty_save", "ic_clubparty_save_jpg", "ic_clubparty_seemore", "ic_competition", "ic_competition_edit_btn_click",
        "ic_competition_save", "ic_competition_save_jpg", "ic_competition_save_pdf", "ic_competition_save_png", "ic_competition_seemore",
        "ic_cradleceremony", "ic_cradleceremony_edit_btn_click", "ic_cradleceremony_save", "ic_cradleceremony_save_jpg",
        "ic_cradleceremony_seemore", "ic_events", "ic_events_edit_btn_click", "ic_events_save", "ic_events_save_jpg",
        "ic_events_save_pdf", "ic_events_save_png", "ic_events_seemore", "ic_exit_no_clicked", "ic_exit_popup_open",
        "ic_exit_savedraft_clicked", "ic_exit_yes_clicked", "ic_farewell", "ic_farewell_edit_btn_click", "ic_farewell_save",
        "ic_farewell_save_jpg", "ic_farewell_save_pdf", "ic_farewell_save_png", "ic_farewell_seemore", "ic_foodparty",
        "ic_foodparty_edit_btn_click", "ic_foodparty_save", "ic_foodparty_save_jpg", "ic_foodparty_seemore", "ic_funeral",
        "ic_funeral_edit_btn_click", "ic_funeral_save", "ic_funeral_save_jpg", "ic_funeral_save_pdf", "ic_funeral_seemore",
        "ic_gamenight", "ic_gamenight_edit_btn_click", "ic_gamenight_save", "ic_gamenight_save_jpg", "ic_gamenight_save_pdf",
        "ic_gamenight_seemore", "ic_genderreveal", "ic_genderreveal_edit_btn_click", "ic_genderreveal_save", "ic_genderreveal_save_jpg",
        "ic_genderreveal_save_pdf", "ic_genderreveal_seemore", "ic_gettogether", "ic_gettogether_edit_btn_click", "ic_gettogether_save",
        "ic_gettogether_save_jpg", "ic_gettogether_seemore", "ic_grandopening", "ic_grandopening_edit_btn_click", "ic_grandopening_save",
        "ic_grandopening_save_jpg", "ic_grandopening_save_pdf", "ic_grandopening_save_png", "ic_grandopening_seemore",
        "ic_haldiceremony", "ic_haldiceremony_edit_btn_click", "ic_haldiceremony_save", "ic_haldiceremony_save_jpg",
        "ic_haldiceremony_save_pdf", "ic_haldiceremony_save_png", "ic_haldiceremony_seemore", "ic_holidayparty",
        "ic_holidayparty_edit_btn_click", "ic_holidayparty_save", "ic_holidayparty_save_jpg", "ic_holidayparty_seemore",
        "ic_housewarming", "ic_housewarming_edit_btn_click", "ic_housewarming_save", "ic_housewarming_save_jpg",
        "ic_housewarming_save_pdf", "ic_housewarming_save_png", "ic_housewarming_seemore", "ic_independenceday",
        "ic_independenceday_edit_btn_click", "ic_independenceday_seemore", "ic_invitationcard_save", "ic_invitationcard_save_jpg",
        "ic_invitationcards_save", "ic_invitationcards_save_jpg", "ic_invitationcards_save_pdf", "ic_invitationcards_save_png",
        "ic_kittyparty", "ic_kittyparty_edit_btn_click", "ic_kittyparty_save", "ic_kittyparty_save_jpg", "ic_kittyparty_save_pdf",
        "ic_kittyparty_seemore", "ic_mehndiceremony", "ic_mehndiceremony_edit_btn_click", "ic_mehndiceremony_save",
        "ic_mehndiceremony_save_jpg", "ic_mehndiceremony_save_pdf", "ic_mehndiceremony_seemore", "ic_movienightparty",
        "ic_movienightparty_edit_btn_click", "ic_movienightparty_save", "ic_movienightparty_save_jpg", "ic_movienightparty_seemore",
        "ic_mundanceremony", "ic_mundanceremony_edit_btn_click", "ic_mundanceremony_save", "ic_mundanceremony_save_jpg",
        "ic_mundanceremony_seemore", "ic_namingceremony", "ic_namingceremony_edit_btn_click", "ic_namingceremony_save",
        "ic_namingceremony_save_jpg", "ic_namingceremony_save_pdf", "ic_namingceremony_seemore", "ic_navratri",
        "ic_navratri_edit_btn_click", "ic_navratri_save", "ic_navratri_save_jpg", "ic_navratri_save_pdf", "ic_navratri_save_png",
        "ic_navratri_seemore", "ic_newyearparty", "ic_newyearparty_edit_btn_click", "ic_newyearparty_save", "ic_newyearparty_save_jpg",
        "ic_newyearparty_seemore", "ic_openhouseparty", "ic_openhouseparty_edit_btn_click", "ic_openhouseparty_save",
        "ic_openhouseparty_save_jpg", "ic_openhouseparty_seemore", "ic_picnic", "ic_picnic_edit_btn_click", "ic_picnic_save",
        "ic_picnic_save_jpg", "ic_picnic_seemore", "ic_pooja", "ic_pooja_edit_btn_click", "ic_pooja_save", "ic_pooja_save_jpg",
        "ic_pooja_save_pdf", "ic_pooja_save_png", "ic_pooja_seemore", "ic_princessparty", "ic_princessparty_edit_btn_click",
        "ic_princessparty_save", "ic_princessparty_save_jpg", "ic_princessparty_save_pdf", "ic_princessparty_seemore",
        "ic_pro_buypro_clicked", "ic_pro_open", "ic_pro_watchad", "ic_reception", "ic_reception_edit_btn_click",
        "ic_reception_save", "ic_reception_save_jpg", "ic_reception_save_pdf", "ic_reception_save_png", "ic_reception_seemore",
        "ic_religiousparty", "ic_religiousparty_edit_btn_click", "ic_religiousparty_save", "ic_religiousparty_save_jpg",
        "ic_religiousparty_save_pdf", "ic_religiousparty_save_png", "ic_religiousparty_seemore", "ic_ringceremony",
        "ic_ringceremony_edit_btn_click", "ic_ringceremony_save", "ic_ringceremony_save_jpg", "ic_ringceremony_save_pdf",
        "ic_ringceremony_save_png", "ic_ringceremony_seemore", "ic_savethedate", "ic_savethedate_edit_btn_click",
        "ic_savethedate_save", "ic_savethedate_save_jpg", "ic_savethedate_save_pdf", "ic_savethedate_seemore", "ic_sleepover",
        "ic_sleepover_edit_btn_click", "ic_sleepover_save", "ic_sleepover_save_jpg", "ic_sleepover_seemore", "ic_sweetsixteen",
        "ic_sweetsixteen_edit_btn_click", "ic_sweetsixteen_save", "ic_sweetsixteen_save_jpg", "ic_sweetsixteen_save_pdf",
        "ic_sweetsixteen_save_png", "ic_sweetsixteen_seemore", "ic_teaparty", "ic_teaparty_edit_btn_click", "ic_teaparty_save",
        "ic_teaparty_save_jpg", "ic_teaparty_seemore", "ic_wedding", "ic_wedding_edit_btn_click", "ic_wedding_save",
        "ic_wedding_save_jpg", "ic_wedding_save_pdf", "ic_wedding_save_png", "ic_wedding_seemore", "icon_btn",
        "image_capture_from_camera", "image_import_from_gallery", "img_bg_btn", "img_bg_buypro_clicked", "img_bg_pro_ad_watched",
        "img_bg_pro_open", "import_element_btn", "in_app_purchase", "independenceday_element_btn", "independenceday_element_used",
        "instagram_share_btn", "instagrampost_bg_clicked", "instagrampost_bg_used", "instagramstory_bg_clicked",
        "instagramstory_bg_used", "int_ad_failed_to_load", "int_ad_failed_to_show", "int_ad_loaded", "int_ad_show",
        "internet_slow_error_popup_open", "internet_slow_error_popup_retry_click", "interstitial_ad_backup_loading_failed",
        "interstitial_ad_loading_failed", "invitationcards_bg_clicked", "invitationcards_bg_used", "janmashtami_element_btn",
        "janmashtami_element_used", "jmc_fb_clicked", "jmc_insta_clicked", "jmc_popup_open", "jmc_x_clicked", "jmc_youtube_clicked",
        "join_dash_share_btn", "join_side_fb_btn", "join_side_insta_btn", "join_side_twitter_btn", "join_side_ytube_btn",
        "labourday_element_btn", "labourday_element_used", "language_arabic_selected", "language_bengali_selected",
        "language_chinese_selected", "language_english_selected", "language_french_selected", "language_german_selected",
        "language_gujarati_selected", "language_hindi_selected", "language_indonesian_selected", "language_japanese_selected",
        "language_kannada_selected", "language_marathi_selected", "language_popup_open", "language_portuguese_selected",
        "language_russian_selected", "language_spanish_selected", "language_tamil_selected", "language_telugu_selected",
        "language_turkish_selected", "language_urdu_selected", "language_vietnamese_selected", "layer_select",
        "letsgo_btn", "lg_3dlogos", "lg_3dlogos_edit_btn_click", "lg_3dlogos_save", "lg_3dlogos_save_jpg",
        "lg_3dlogos_save_pdf", "lg_3dlogos_save_png", "lg_3dlogos_seemore", "lg__save", "lg__save_jpg", "lg__save_pdf",
        "lg__save_png", "lg_advertising", "lg_advertising_edit_btn_click", "lg_advertising_save", "lg_advertising_save_jpg",
        "lg_advertising_save_pdf", "lg_advertising_seemore", "lg_agriculture", "lg_agriculture_edit_btn_click", "lg_agriculture_save",
        "lg_agriculture_save_jpg", "lg_agriculture_save_png", "lg_agriculture_seemore", "lg_alphabetic", "lg_alphabetic_edit_btn_click",
        "lg_alphabetic_save", "lg_alphabetic_save_jpg", "lg_alphabetic_save_png", "lg_alphabetic_seemore", "lg_animals_birds",
        "lg_animals_birds_edit_btn_click", "lg_architecture", "lg_architecture_edit_btn_click", "lg_architecture_save",
        "lg_architecture_save_jpg", "lg_architecture_seemore", "lg_art_design", "lg_art_design_edit_btn_click", "lg_automobile",
        "lg_automobile_edit_btn_click", "lg_automobile_save", "lg_automobile_save_jpg", "lg_automobile_save_png", "lg_automobile_seemore",
        "lg_barber", "lg_barber_edit_btn_click", "lg_barber_save", "lg_barber_save_jpg", "lg_barber_save_png", "lg_barber_seemore",
        "lg_black_white", "lg_black_white_edit_btn_click", "lg_btn_click",
        "lg_business", "lg_business_edit_btn_click", "lg_business_save", "lg_business_save_jpg", "lg_business_save_pdf",
        "lg_business_save_png", "lg_business_seemore", "lg_colorful", "lg_colorful_edit_btn_click", "lg_colorful_save",
        "lg_colorful_save_jpg", "lg_colorful_seemore", "lg_communication", "lg_communication_edit_btn_click", "lg_communication_save",
        "lg_communication_save_jpg", "lg_communication_save_pdf", "lg_communication_save_png", "lg_communication_seemore",
        "lg_cricket", "lg_cricket_edit_btn_click", "lg_cricket_save", "lg_cricket_save_jpg", "lg_cricket_save_pdf",
        "lg_cricket_seemore", "lg_dance", "lg_dance_edit_btn_click", "lg_dance_save", "lg_dance_save_jpg",
        "lg_dance_save_pdf", "lg_dance_save_png", "lg_dance_seemore", "lg_devotional_seemore", "lg_doodle",
        "lg_doodle_edit_btn_click", "lg_doodle_save", "lg_doodle_save_jpg", "lg_doodle_seemore", "lg_ecommerce",
        "lg_ecommerce_edit_btn_click", "lg_ecommerce_save", "lg_ecommerce_save_jpg", "lg_ecommerce_seemore", "lg_education",
        "lg_education_edit_btn_click", "lg_education_save", "lg_education_save_jpg", "lg_education_save_png", "lg_education_seemore",
        "lg_esports", "lg_esports_edit_btn_click", "lg_esports_save", "lg_esports_save_jpg", "lg_esports_save_pdf",
        "lg_esports_save_png", "lg_esports_seemore", "lg_exit_no_clicked", "lg_exit_popup_open", "lg_exit_savedraft_clicked",
        "lg_exit_yes_clicked", "lg_fashion", "lg_fashion_edit_btn_click", "lg_fashion_save", "lg_fashion_save_jpg",
        "lg_fashion_save_pdf", "lg_fashion_save_png", "lg_fashion_seemore", "lg_festival_seemore", "lg_fintech",
        "lg_fintech_edit_btn_click", "lg_fintech_save", "lg_fintech_save_jpg", "lg_fintech_save_pdf", "lg_fintech_save_png",
        "lg_fintech_seemore", "lg_fitness", "lg_fitness_edit_btn_click", "lg_fitness_save", "lg_fitness_save_jpg",
        "lg_fitness_seemore", "lg_food_drink", "lg_food_drink_edit_btn_click", "lg_game", "lg_game_edit_btn_click",
        "lg_game_save", "lg_game_save_jpg", "lg_game_save_pdf", "lg_game_seemore", "lg_goodmorning_seemore", "lg_goodthoughts_seemore",
        "lg_handwriting", "lg_handwriting_edit_btn_click", "lg_handwriting_save", "lg_handwriting_save_jpg", "lg_handwriting_save_pdf",
        "lg_handwriting_save_png", "lg_handwriting_seemore", "lg_health", "lg_health_edit_btn_click", "lg_health_save",
        "lg_health_save_jpg", "lg_health_seemore", "lg_heart", "lg_heart_edit_btn_click", "lg_heart_save", "lg_heart_save_jpg",
        "lg_heart_save_png", "lg_heart_seemore", "lg_inaugurations", "lg_jewellery", "lg_jewellery_edit_btn_click", "lg_jewellery_save",
        "lg_jewellery_save_jpg", "lg_jewellery_seemore", "lg_law_attorney", "lg_law_attorney_edit_btn_click", "lg_leadersquotes_seemore",
        "lg_logos_edit_btn_click", "lg_logos_save", "lg_logos_save_jpg", "lg_logos_save_pdf", "lg_logos_save_png",
        "lg_maintenance", "lg_maintenance_edit_btn_click", "lg_maintenance_save", "lg_maintenance_save_jpg", "lg_maintenance_save_pdf",
        "lg_maintenance_save_png", "lg_maintenance_seemore", "lg_makeup", "lg_makeup_edit_btn_click", "lg_makeup_save",
        "lg_makeup_save_jpg", "lg_makeup_seemore", "lg_music", "lg_music_edit_btn_click", "lg_music_save", "lg_music_save_jpg",
        "lg_music_save_png", "lg_music_seemore", "lg_nail_art", "lg_nail_art_edit_btn_click", "lg_photography",
        "lg_photography_edit_btn_click", "lg_photography_save", "lg_photography_save_jpg", "lg_photography_save_pdf",
        "lg_photography_save_png", "lg_photography_seemore", "lg_pro_buypro_clicked", "lg_pro_open", "lg_pro_watchad",
        "lg_quotes", "lg_realestate", "lg_realestate_edit_btn_click", "lg_realestate_save", "lg_realestate_save_jpg",
        "lg_realestate_save_pdf", "lg_realestate_save_png", "lg_realestate_seemore", "lg_religious", "lg_religious_edit_btn_click",
        "lg_religious_save", "lg_religious_save_jpg", "lg_religious_seemore", "lg_restaurant", "lg_restaurant_edit_btn_click",
        "lg_restaurant_save", "lg_restaurant_save_jpg", "lg_restaurant_seemore", "lg_rounded", "lg_rounded_edit_btn_click",
        "lg_rounded_save", "lg_rounded_save_jpg", "lg_rounded_seemore", "lg_security", "lg_security_edit_btn_click",
        "lg_security_save", "lg_security_save_jpg", "lg_security_seemore", "lg_socialcare", "lg_socialcare_edit_btn_click",
        "lg_socialcare_save", "lg_socialcare_save_jpg", "lg_socialcare_save_png", "lg_socialcare_seemore", "lg_stampcard",
        "lg_stampcard_edit_btn_click", "lg_stampcard_seemore", "lg_sword_wings", "lg_sword_wings_edit_btn_click", "lg_technology",
        "lg_technology_edit_btn_click", "lg_technology_save", "lg_technology_save_jpg", "lg_technology_save_pdf",
        "lg_technology_save_png", "lg_technology_seemore", "lg_textile", "lg_textile_edit_btn_click", "lg_textile_save",
        "lg_textile_save_jpg", "lg_textile_seemore", "lg_travel", "lg_travel_edit_btn_click", "lg_travel_save", "lg_travel_save_jpg",
        "lg_travel_save_png", "lg_travel_seemore", "lg_vintage", "lg_vintage_edit_btn_click", "lg_vintage_save",
        "lg_vintage_save_jpg", "lg_vintage_save_png", "lg_vintage_seemore", "lg_watercolor", "lg_watercolor_edit_btn_click",
        "lg_watercolor_save", "lg_watercolor_save_jpg", "lg_watercolor_save_pdf", "lg_watercolor_save_png", "lg_watercolor_seemore",
        "lifestyle_element_btn", "lifestyle_element_used", "linkedinpost_bg_clicked", "linkedinpost_bg_used", "loader_ended",
        "logos_bg_clicked", "logos_bg_used", "lohri_element_btn", "lohri_element_used", "loose_popup_dashbord_loose_btn",
        "loose_popup_dashbord_sub_btn", "loose_popup_sharescrn_loose_btn", "loose_popup_sharescrn_sub_btn", "love_element_btn",
        "love_element_used", "mahashivratri_element_btn", "mahashivratri_element_used", "makarsankranti_element_btn",
        "makarsankranti_element_used", "mandala_element_btn", "mandala_element_used", "menu_help_clicked", "menu_how_to_use_clicked",
        "menu_more_apps_clicked", "menu_multi_language_clicked", "menu_my_account_clicked", "menu_privacy_policy_clicked",
        "menu_profile_clicked", "menu_rate_us_clicked", "menu_share_clicked", "menu_support_clicked", "menu_user_guide_clicked",
        "menu_xp_store_clicked", "message_btn_click", "metaverse_element_btn", "metaverse_element_used", "mockup_element_btn",
        "mockup_element_used", "monoline_element_btn", "monoline_element_used", "morphism_element_btn", "morphism_element_used",
        "mp_purchase_dont_loosepopup", "my_account_delete_account_clicked", "my_account_share_clicked", "my_account_sign_in_google_clicked",
        "my_account_signout_clicked", "my_subscription_click", "native_ad_backup_loading_failed", "native_ad_loading_failed",
        "navratri_element_btn", "navratri_element_used", "neongraphic_element_btn", "neongraphic_element_used", "new_day1_content_count",
        "new_day1_no_content_count", "new_removead_popup_loveads_click", "new_removead_popup_open", "new_removead_popup_removead_click",
        "newyear_element_btn", "newyear_element_used", "nointernetconnection", "normal_poster_template_continue_click",
        "normal_poster_template_edit_click", "notification_foreground", "notification_open", "notification_receive", "nudge_btn",
        "numeric_element_btn", "numeric_element_used", "onboard_1st_screen_next", "onboard_1st_screen_skip", "onboard_1st_screen_visible",
        "onboard_2nd_screen_next", "onboard_2nd_screen_skip", "onboard_2nd_screen_visible", "onboard_3rd_screen_next",
        "onboard_3rd_screen_skip", "onboard_3rd_screen_visible",
        "onboard_4th_screen_next", "onboard_4th_screen_skip", "onboard_4th_screen_visible", "opacity_btn", "ornaments_element_btn",
        "ornaments_element_used", "os_update", "paid_ad_impression", "paper_element_btn", "paper_element_used", "photocollage_bg_clicked",
        "photocollage_bg_used", "pickcolor_bg_buypro_clicked", "pickcolor_bg_pro_ad_watched", "plastic_element_btn", "plastic_element_used",
        "pongal_element_btn", "pongal_element_used", "prefered_content_screen_cnw_click", "prefered_content_screen_design_click",
        "prefered_content_screen_moredesign_click", "prefered_content_screen_skip_click", "prefered_content_screen_visible",
        "pro_clicked_from_dashboard", "pro_clicked_from_menu", "pro_monthly_clicked", "pro_monthly_continue_clicked", "pro_screen_close",
        "pro_screen_open", "pro_weekly_clicked", "pro_weekly_continue_clicked", "pro_yearly_clicked", "pro_yearly_continue_clicked",
        "profile_btn", "profile_btn_click", "profile_edit_btn", "profile_save_btn", "profile_upload_btn", "purchase_status", "quotes_bg_clicked",
        "quotes_bg_used", "rakshabandhan_element_btn", "rakshabandhan_element_used", "ramadan_element_btn", "ramadan_element_used",
        "ramnavmi_element_btn", "ramnavmi_element_used", "redo_used", "remove_ai_watermark_popup_open", "remove_bg_auto_clicked",
        "remove_bg_button_click", "remove_bg_eraser_clicked", "remove_bg_help_clicked", "remove_bg_human_clicked", "remove_bg_lasso_clicked",
        "remove_bg_object_clicked", "remove_bg_refine_edge_clicked", "remove_bg_refine_save_clicked", "remove_bg_reset_clicked",
        "remove_bg_restore_clicked", "remove_bg_save_clicked", "remove_bg_zoom_clicked", "remove_watermark_ad_watched", "remove_watermark_btn_click",
        "remove_watermark_one_time_btn_clicked", "remove_watermark_pro_clicked", "remove_watermark_watch_video_clicked", "replace_img_btn",
        "republicday_element_btn", "republicday_element_used", "reset_no_clicked", "reset_popup_open", "reset_yes_clicked",
        "response_failed_time", "result_failed_time", "retro_element_btn", "retro_element_used", "reward_ad_close", "reward_ad_failed_to_load",
        "reward_ad_failed_to_show", "reward_ad_not_available", "reward_ad_show", "rewarded_ad_backup_loading_failed",
        "rewarded_ad_loading_failed", "rotation_btn", "sale_element_btn", "sale_element_used", "save_as_darft_btn", "save_jpg_pro_ad_watched",
        "save_jpg_pro_buypro_clicked", "save_jpg_pro_open", "save_pdf_pro_ad_watched", "save_pdf_pro_buypro_clicked", "save_pdf_pro_open",
        "save_png_pro_ad_watched", "save_png_pro_buypro_clicked", "save_png_pro_open", "saved_jpg_high", "saved_jpg_low", "saved_jpg_medium",
        "saved_pdf_high", "saved_png_high", "saved_png_low", "saved_png_medium", "seall_search_clicked", "search_btn", "search_dp_content_clicked",
        "search_fl_content_clicked", "search_ft_content_clicked", "search_ic_content_clicked", "search_lg_content_clicked", "search_no_result_found",
        "search_sm_content_clicked", "search_st_content_clicked", "search_vc_content_clicked", "seeall_cnw_facebookcovers",
        "seeall_cnw_facebookpost", "seeall_cnw_fl", "seeall_cnw_ft", "seeall_cnw_ic", "seeall_cnw_instagrampost", "seeall_cnw_instagramstory",
        "seeall_cnw_lg", "seeall_cnw_linkedinpost", "seeall_cnw_photocollage", "seeall_cnw_quotes", "seeall_cnw_st", "seeall_cnw_vc",
        "seeall_cnw_whatsappstatus", "seeall_cnw_youtubebanner", "seeall_cnw_youtubethumbnails", "session_start", "shadow_buypro_click",
        "shadow_click", "shadow_pro_open", "shadow_text_ad_watched", "shadow_text_share_clicked", "shapes_element_btn", "shapes_element_used",
        "share_screen_remove_watermark_ad_watched", "share_screen_remove_watermark_btn_click", "share_screen_watermark_visible",
        "shared_with_other_source", "siblingsday_element_btn", "siblingsday_element_used", "size_btn", "sm__save", "sm__save_jpg",
        "sm__save_pdf", "sm__save_png", "sm_btn_click", "sm_exit_no_clicked", "sm_exit_popup_open", "sm_exit_savedraft_clicked",
        "sm_exit_yes_clicked", "sm_facebookcovers", "sm_facebookcovers_edit_btn_click", "sm_facebookcovers_save", "sm_facebookcovers_save_jpg",
        "sm_facebookcovers_save_pdf", "sm_facebookcovers_seemore", "sm_facebookpost", "sm_facebookpost_edit_btn_click", "sm_facebookpost_save",
        "sm_facebookpost_save_jpg", "sm_facebookpost_save_pdf", "sm_facebookpost_save_png", "sm_facebookpost_seemore", "sm_instagrampost",
        "sm_instagrampost_edit_btn_click", "sm_instagrampost_save", "sm_instagrampost_save_jpg", "sm_instagrampost_save_pdf",
        "sm_instagrampost_save_png", "sm_instagrampost_seemore", "sm_instagramstory", "sm_instagramstory_edit_btn_click",
        "sm_instagramstory_save", "sm_instagramstory_save_jpg", "sm_instagramstory_save_pdf", "sm_instagramstory_save_png",
        "sm_instagramstory_seemore", "sm_linkedinpost", "sm_linkedinpost_edit_btn_click", "sm_linkedinpost_save", "sm_linkedinpost_save_jpg",
        "sm_linkedinpost_save_pdf", "sm_linkedinpost_save_png", "sm_linkedinpost_seemore", "sm_photocollage", "sm_photocollage_edit_btn_click",
        "sm_photocollage_save", "sm_photocollage_save_jpg", "sm_photocollage_save_png", "sm_photocollage_seemore", "sm_pro_buypro_clicked",
        "sm_pro_open", "sm_pro_watchad", "sm_quotes", "sm_quotes_edit_btn_click", "sm_quotes_save", "sm_quotes_save_jpg",
        "sm_quotes_save_png", "sm_quotes_seemore", "sm_whatsappstatus", "sm_whatsappstatus_edit_btn_click", "sm_whatsappstatus_save",
        "sm_whatsappstatus_save_jpg", "sm_whatsappstatus_save_pdf", "sm_whatsappstatus_save_png", "sm_whatsappstatus_seemore",
        "sm_youtubebanner", "sm_youtubebanner_edit_btn_click", "sm_youtubebanner_save", "sm_youtubebanner_save_jpg",
        "sm_youtubebanner_save_pdf", "sm_youtubebanner_save_png", "sm_youtubebanner_seemore", "sm_youtubethumbnails",
        "sm_youtubethumbnails_edit_btn_click", "sm_youtubethumbnails_save", "sm_youtubethumbnails_save_jpg", "sm_youtubethumbnails_save_pdf",
        "sm_youtubethumbnails_save_png", "sm_youtubethumbnails_seemore", "socialmedia_element_btn", "socialmedia_element_used",
        "solid_bg_btn", "space_btn", "sparkles_element_btn", "sparkles_element_used", "spinwheel_free_used", "spinwheel_open_homescreen",
        "spinwheel_open_taskcenter", "spinwheel_watch_ad", "spiritual_element_btn", "spiritual_element_used", "splash_guest_clicked",
        "splash_referral_code_skip", "splash_signin_google_clicked", "sports_element_btn", "sports_element_used", "st_content",
        "st_content_edit_btn_click", "st_exit_no_clicked", "st_exit_popup_open", "st_exit_savedraft_clicked", "st_exit_yes_clicked",
        "st_pro_open", "st_pro_watchad", "st_stampcard_save", "st_stampcard_save_jpg", "st_stampcard_save_png", "st_stampcard_seemore",
        "stamp_element_btn", "stamp_element_used", "step1_5_homescreen_data_loaded", "step1_homescreen_launched", "step2_content_edit_screen_open",
        "step3_content_saved", "support_btn_click", "tag_selection_next", "tag_selection_onback_press", "tag_selection_screen_visible",
        "tag_selection_skip", "task_center_dailybonus_click", "task_center_refer_a_friend_click", "task_center_save_template_click",
        "task_center_spinwheel_click", "task_center_watchad_click", "taskcenter_watch_ad_0", "taskcenter_watch_ad_1",
        "taskcenter_watchad_high_reward_lost", "tattoo_element_btn", "tattoo_element_used", "text_btn", "text_image_ai_btn_click",
        "top_banner_astrozop_clicked", "top_banner_criczop_clicked", "top_banner_gamezop_clicked", "top_banner_newszop_clicked",
        "top_banner_quizzop_clicked", "total_cnw_save", "total_content_save", "total_fl_save", "total_ft_save", "total_ic_save",
        "total_lg_save", "total_sm_save", "total_st_save", "total_vc_save", "tr_ai_chat_btn_click", "tr_ai_chat_business_catgory_selected",
        "tr_ai_chat_caption_catgory_selected", "tr_ai_chat_fun_catgory_selected", "tr_ai_chat_lable_clicked", "tr_ai_chat_love_catgory_selected",
        "tr_ai_chat_social_catgory_selected", "tr_ai_chat_work_catgory_selected", "tr_ai_chat_writing_catgory_selected",
        "tr_ai_img_lable_clicked", "tr_ai_lable_inbetween_clicked", "tr_ai_poster_lable_clicked", "tr_ai_toggle_btn_click", "tr_btn_click",
        "tr_daily_pick_lable_clicked", "tr_discover_aiart_clicked", "tr_discover_aiart_seeall_clicked", "tr_event_lable_clicked", "tr_events_seemore",
        "tr_fl_content_click", "tr_ft_content_click", "tr_game_icon_click", "tr_game_lable_clicked", "tr_ic_content_click",
        "tr_lg_content_click", "tr_profile_lable_clicked", "tr_sm_content_click", "tr_subscription1_lable_clicked", "tr_subscription_lable_clicked",
        "tr_text_image_ai_btn_click", "tr_vc_content_click", "travel_element_btn", "travel_element_used", "trending_bottom_hit_1time",
        "undo_used", "usa_element_btn", "usa_element_used", "valentinesday_element_btn", "valentinesday_element_used",
        "vasantpanchami_element_btn", "vasantpanchami_element_used", "vc__save", "vc__save_jpg", "vc__save_png", "vc_art_design",
        "vc_art_design_edit_btn_click", "vc_automobile", "vc_automobile_edit_btn_click", "vc_automobile_save", "vc_automobile_save_jpg",
        "vc_automobile_save_pdf", "vc_automobile_seemore", "vc_beauty_salon", "vc_beauty_salon_edit_btn_click", "vc_btn_click",
        "vc_business", "vc_business_edit_btn_click", "vc_business_save", "vc_business_save_jpg", "vc_business_save_pdf",
        "vc_business_save_png", "vc_business_seemore", "vc_corporate", "vc_corporate_edit_btn_click", "vc_corporate_save",
        "vc_corporate_save_jpg", "vc_corporate_save_pdf", "vc_corporate_seemore", "vc_education", "vc_education_edit_btn_click",
        "vc_education_save", "vc_education_save_jpg", "vc_education_save_pdf", "vc_education_seemore", "vc_entertainmnet",
        "vc_entertainmnet_edit_btn_click", "vc_entertainmnet_save", "vc_entertainmnet_save_jpg", "vc_entertainmnet_save_png",
        "vc_entertainmnet_seemore", "vc_eventplanner", "vc_eventplanner_edit_btn_click", "vc_eventplanner_save", "vc_eventplanner_save_jpg",
        "vc_eventplanner_seemore", "vc_exit_no_clicked", "vc_exit_popup_open", "vc_exit_savedraft_clicked", "vc_exit_yes_clicked",
        "vc_fashion", "vc_fashion_edit_btn_click", "vc_fashion_save", "vc_fashion_save_jpg", "vc_fashion_save_pdf",
        "vc_fashion_seemore", "vc_fitness", "vc_fitness_edit_btn_click", "vc_fitness_save", "vc_fitness_save_jpg",
        "vc_fitness_seemore", "vc_food", "vc_food_edit_btn_click", "vc_food_save", "vc_food_save_jpg", "vc_food_seemore",
        "vc_homeservice", "vc_homeservice_edit_btn_click", "vc_homeservice_save", "vc_homeservice_save_jpg", "vc_homeservice_save_pdf",
        "vc_homeservice_save_png", "vc_homeservice_seemore", "vc_jewellery", "vc_jewellery_edit_btn_click", "vc_jewellery_save",
        "vc_jewellery_save_jpg", "vc_jewellery_seemore", "vc_lawyer", "vc_lawyer_edit_btn_click", "vc_lawyer_save", "vc_lawyer_save_jpg",
        "vc_lawyer_seemore", "vc_medical", "vc_medical_edit_btn_click", "vc_medical_save", "vc_medical_save_jpg", "vc_medical_seemore",
        "vc_photography", "vc_photography_edit_btn_click", "vc_photography_save", "vc_photography_save_jpg", "vc_photography_seemore",
        "vc_pro_buypro_clicked", "vc_pro_open", "vc_pro_watchad", "vc_realestate", "vc_realestate_edit_btn_click", "vc_realestate_save",
        "vc_realestate_save_jpg", "vc_realestate_save_pdf", "vc_realestate_seemore", "vc_spa_massage", "vc_spa_massage_edit_btn_click",
        "vc_technology", "vc_technology_edit_btn_click", "vc_technology_save", "vc_technology_save_jpg", "vc_technology_seemore",
        "vc_travel", "vc_travel_edit_btn_click", "vc_travel_save", "vc_travel_save_jpg", "vc_travel_save_pdf", "vc_travel_seemore",
        "vc_visitingcards_edit_btn_click", "vc_visitingcards_save", "vc_visitingcards_save_jpg", "vc_visitingcards_save_pdf",
        "vc_visitingcards_save_png", "visitingcards_bg_clicked", "visitingcards_bg_used", "watch_tutorial_btn", "wedding_element_btn",
        "wedding_element_used", "whatsapp_share_btn", "whatsappstatus_bg_clicked", "whatsappstatus_bg_used", "womensday_element_btn",
        "womensday_element_used", "xp_earn_menu_click", "xp_signin_bonus_collected", "xp_signin_bonus_popup_open", "xp_store_info_clicked",
        "xp_store_share_app_clicked", "xp_store_sign_in_google_clicked", "yml_dp_clicked", "yml_fl_clicked", "yml_ft_clicked",
        "yml_ic_clicked", "yml_lg_clicked", "yml_sm_clicked", "yml_unknowncategory_clicked", "yml_vc_clicked", "you_may_like_content_clicked",
        "youthday_element_btn", "youthday_element_used", "youtubebanner_bg_clicked", "youtubebanner_bg_used", "youtubethumbnails_bg_clicked",
        "youtubethumbnails_bg_used", "zodiac_element_btn", "zodiac_element_used"
    ]
    included_events = [
        "first_open", "step1_homescreen_launched", "step2_content_edit_screen_open", "step3_content_saved"
    ]
    if file:
        # Read the CSV file
        df = pd.read_csv(file)
        #st.title("Analysis of User Removal and Churn Events in the Loogy App🐶")
        with st.spinner('Please wait, results are being processed...'):
            df['event_time_UTC'] = pd.to_datetime(df['event_time_UTC'], errors='coerce', utc=True)
            df['event_date'] = df['event_time_UTC'].dt.date

        st.write("Original Data:")
        st.dataframe(df)



        unique_ids = df['user_pseudo_id'].unique()
        unique_events = df['event_name'].unique()
        unique_dates = df['event_date'].unique()

        # User Pseudo ID filter
        selected_user_ids = st.sidebar.multiselect("Select User Pseudo ID", options=unique_ids)

        # Event Name filter
        selected_events = st.sidebar.multiselect("Select Event Name", options=unique_events)

        # Event Date filter
        selected_dates = st.sidebar.multiselect("Select Event Date", options=unique_dates)

        # Apply filters to the DataFrame
        if selected_user_ids:
            df = df[df['user_pseudo_id'].isin(selected_user_ids)]

        if selected_events:
            df = df[df['event_name'].isin(selected_events)]

        if selected_dates:
            df = df[df['event_date'].isin(selected_dates)]


        # Sort by 'user_pseudo_id' and 'event_time_UTC' to get the correct order
        df_sorted = df.sort_values(by=['user_pseudo_id', 'event_time_UTC'])

        # Function to get the last valid record for each user
        def get_valid_last_record(group):
            # Reverse the group to check from last to first
            group_reversed = group[::-1]

            for index, row in group_reversed.iterrows():
                if row['event_name'] not in excluded_events:
                    return row

            # If all records are in the excluded list, return the actual last one
            return group_reversed.iloc[0]

        # Apply the function to get the last valid record for each user
        last_record_df = df_sorted.groupby('user_pseudo_id').apply(get_valid_last_record).reset_index(drop=True)

        st.write("Last Valid Record for Each User:")
        st.dataframe(last_record_df)

        app_remove_users = last_record_df[last_record_df['event_name'] == 'app_remove']['user_pseudo_id'].unique()
        app_remove_df = df_sorted[df_sorted['user_pseudo_id'].isin(app_remove_users)]

        # Function to get the last 5 valid records for each user
        def get_last_5_valid_records(group):
            valid_records = group[~group['event_name'].isin(excluded_events)]
            return valid_records.tail(5)

        last_5_records_df1 = app_remove_df.groupby('user_pseudo_id').apply(get_last_5_valid_records).reset_index(drop=True)

        #st.write("Last 5 Valid Records for Users with 'app_remove' Event:")
        #st.dataframe(last_5_records_df1)

        non_app_remove_users = last_record_df[last_record_df['event_name'] != 'app_remove']['user_pseudo_id'].unique()
        non_app_remove_df = df_sorted[df_sorted['user_pseudo_id'].isin(non_app_remove_users)]

        def get_last_5_valid_records(group):
            valid_records = group[~group['event_name'].isin(excluded_events)]
            return valid_records.tail(5)

        last_5_records_df2 = non_app_remove_df.groupby('user_pseudo_id').apply(get_last_5_valid_records).reset_index(drop=True)

        #st.write("Last 5 Valid Records for Users without 'app_remove' Event:")
        #st.dataframe(last_5_records_df2)

        app_remove_users = last_record_df[last_record_df['event_name'] == 'app_remove']['user_pseudo_id'].unique()
        app_remove_df = df_sorted[df_sorted['user_pseudo_id'].isin(app_remove_users)]

        # Function to get the last 5 valid records for each user
        def get_last_5_valid_records(group):
            valid_records = group[~group['event_name'].isin(excluded_events + ['app_remove'])]
            return valid_records.tail(5)

        last_5_records_df1 = app_remove_df.groupby('user_pseudo_id').apply(get_last_5_valid_records).reset_index(drop=True)

        #st.write("Last 5 Valid Records for Users with 'app_remove' Event (excluding 'app_remove'):")
        #st.dataframe(last_5_records_df1)

        # Create a pivot table for event_name by Total users
        pivot_table = last_record_df.groupby('event_name').size().reset_index(name='Total users')

        # Sort the pivot table in descending order
        pivot_table = pivot_table.sort_values(by='Total users', ascending=False)

        # Add a percentage column
        pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100

        col1, col2 = st.columns(2)
    # with col1:
        #st.write("Pivot Table of Overall event_name by Total users:")
        #st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))

        filtered_df = df[df['event_name'].isin(included_events)]

        two_event_df = df_sorted[df_sorted['event_name'].isin(['first_open', 'step1_homescreen_launched'])]

        # Get the last record between these two events for each user
        last_between_events_df = two_event_df.groupby('user_pseudo_id').last().reset_index()

        #st.write("Record Between first open and homescreen launched for Each User:")
        #st.dataframe(last_between_events_df)

        users_with_first_open = last_between_events_df[last_between_events_df['event_name'] == 'first_open']['user_pseudo_id']

        # Get the last record from the main data for these users
        final_df = df[df['user_pseudo_id'].isin(users_with_first_open)]
        def get_last_valid_record(group):
            group_reversed = group[::-1]
            for index, row in group_reversed.iterrows():
                if row['event_name'] not in excluded_events:
                    return row
            return group_reversed.iloc[0]

        final_df = final_df.groupby('user_pseudo_id').apply(get_last_valid_record).reset_index(drop=True)

        # Display the final DataFrame
        #st.write("Before homescreen launched user churn:")
        #st.dataframe(final_df)

        pivot_table = final_df.groupby('event_name').size().reset_index(name='Total users')
        pivot_table = pivot_table.sort_values(by='Total users', ascending=False)
        pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100
        with col1:
            st.write("Pivot Table of Before homescreen launched user churn:")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))

            two_event_df = df_sorted[df_sorted['event_name'].isin(['step1_homescreen_launched', 'step2_content_edit_screen_open'])]

            # Get the last record between these two events for each user
            last_between_events_df = two_event_df.groupby('user_pseudo_id').last().reset_index()

            #st.write("Record Between first open and homescreen launched for Each User:")
            #st.dataframe(last_between_events_df)

            users_with_first_open = last_between_events_df[last_between_events_df['event_name'] == 'step1_homescreen_launched']['user_pseudo_id']

            final_df = df[df['user_pseudo_id'].isin(users_with_first_open)]
            def get_last_valid_record(group):
                group_reversed = group[::-1]
                for index, row in group_reversed.iterrows():
                    if row['event_name'] not in excluded_events:
                        return row
                return group_reversed.iloc[0]

            final_df = final_df.groupby('user_pseudo_id').apply(get_last_valid_record).reset_index(drop=True)

            # Display the final DataFrame
            #st.write("Before content_edit_screen_open user churn:")
            #st.dataframe(final_df)

            pivot_table = final_df.groupby('event_name').size().reset_index(name='Total users')
            pivot_table = pivot_table.sort_values(by='Total users', ascending=False)
            pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100
        with col2:
            st.write("Pivot Table of Before content_edit_screen_open user churn:")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))


            pivot_table = last_record_df.groupby('event_name').size().reset_index(name='Total users')
            pivot_table = pivot_table.sort_values(by='Total users', ascending=False)
            pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100
        with col1:
            #st.write("Pivot Table of Overall event_name by Total users:")
            #st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))


            two_event_df = df_sorted[df_sorted['event_name'].isin(['step2_content_edit_screen_open', 'step3_content_saved'])]

            # Get the last record between these two events for each user
            last_between_events_df = two_event_df.groupby('user_pseudo_id').last().reset_index()

            #st.write("Record Between first open and homescreen launched for Each User:")
            #st.dataframe(last_between_events_df)

            users_with_first_open = last_between_events_df[last_between_events_df['event_name'] == 'step2_content_edit_screen_open']['user_pseudo_id']

            final_df = df[df['user_pseudo_id'].isin(users_with_first_open)]
            def get_last_valid_record(group):
                group_reversed = group[::-1]
                for index, row in group_reversed.iterrows():
                    if row['event_name'] not in excluded_events:
                        return row
                return group_reversed.iloc[0]

            final_df = final_df.groupby('user_pseudo_id').apply(get_last_valid_record).reset_index(drop=True)

            # Display the final DataFrame
            #st.write("Before content_saved user churn:")
            #st.dataframe(final_df)

            pivot_table = final_df.groupby('event_name').size().reset_index(name='Total users')
            pivot_table = pivot_table.sort_values(by='Total users', ascending=False)
            pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100
        with col2:
            st.write("Pivot Table of Before content_saved user churn:")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))

            pivot_table = filtered_df.groupby('event_name')['user_pseudo_id'].nunique().reset_index(name='Total unique users')
            first_open_users = pivot_table.loc[pivot_table['event_name'] == 'first_open', 'Total unique users'].values[0]
            pivot_table['Percentage'] = (pivot_table['Total unique users'] / first_open_users) * 100
        with col2:
            st.write("Pivot Table for Specific Events by Total Unique Users:")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))

            # Filter the DataFrame to only include users who have the `step3_content_saved` event
            step3_df = df_sorted[df_sorted['event_name'] == 'step3_content_saved']

            # Get the users who have the `step3_content_saved` event
            users_with_step3_content_saved = step3_df['user_pseudo_id'].unique()

            # Filter the original DataFrame to include only these users
            filtered_df = df_sorted[df_sorted['user_pseudo_id'].isin(users_with_step3_content_saved)]

            # Function to get the last valid record after `step3_content_saved` for each user
            def get_last_valid_record_after_step3(group):
                step3_index = group[group['event_name'] == 'step3_content_saved'].index[0]  # Get the index of `step3_content_saved`
                subsequent_records = group.loc[step3_index + 1:]  # Select records after `step3_content_saved`

                # Reverse the order to check from last to first
                subsequent_records_reversed = subsequent_records[::-1]

                for index, row in subsequent_records_reversed.iterrows():
                    if row['event_name'] not in included_events:
                        return row

                # If all subsequent records are in the included list, return the actual last one
                return subsequent_records.iloc[-1]

            # Apply the function to get the last valid record for each user after `step3_content_saved`
            final_df = filtered_df.groupby('user_pseudo_id').apply(get_last_valid_record_after_step3).reset_index(drop=True)

            # Display the final DataFrame
            #st.write("After content_saved user churn:")
            #st.dataframe(final_df)

            pivot_table = final_df.groupby('event_name').size().reset_index(name='Total users')
            pivot_table = pivot_table.sort_values(by='Total users', ascending=False)
            pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100
        with col1:
            st.write("Pivot Table of After content_saved user churn:")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))


            session_start_df = df[df['event_name'] == 'session_start']
            # Count occurrences of 'session_start' per user
            session_counts = session_start_df.groupby('user_pseudo_id').size()

            # Group by the count to get the number of users who had 1, 2, 3, etc. sessions
            session_count_pivot = session_counts.value_counts().reset_index(name='Total users')
            session_count_pivot.columns = ['Session Count', 'Total users']
            session_count_pivot = session_count_pivot.sort_values(by='Session Count')
            session_count_pivot['Percentage'] = (session_count_pivot['Total users'] /session_count_pivot['Total users'].sum()) * 100
        with col1:
            st.write("Pivot Table of Session by Total Users:")
            st.write(session_count_pivot.style.format({'Percentage': "{:.2f}%"}))

            pivot_table = df.groupby('event_date')['user_pseudo_id'].nunique().reset_index(name='Total unique users')
            pivot_table = pivot_table.sort_values(by='Total unique users', ascending=False)
            pivot_table['Percentage'] = (pivot_table['Total unique users'] /  pivot_table['Total unique users'].max()) * 100
        with col1:
            st.write("Pivot Table of Datewise user churn:")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))

        def get_matching_events(group):
            matching_events = group[group['event_name'].isin(second_event_list)]
            return matching_events[['user_pseudo_id', 'event_name']]

            # Apply the function to the DataFrame to get the matching events
        #matching_events_df = last_5_records_df.groupby('user_pseudo_id').apply(get_matching_events).reset_index(drop=True)
        with col2:
            # Display the table with user ID and matched event
            #st.write("Users and Matched Events from Second Event List:")
            #st.dataframe(matching_events_df)

            total_users = df['user_pseudo_id'].nunique()
            st.sidebar.header('Total Users')
            st.sidebar.write(f"Total Users: {total_users}")

            matched_events_list = [
               "add_img_btn", "addtext_btn", "paid_ad_impression","ai__category_selected", "ai_avatar_category_selected", "ai_avatar_couple_selected",
                "ai_avatar_female_selected", "ai_avatar_male_selected", "ai_avatarai_category_selected", "ai_background_category_selected", "ai_backgroundai_category_selected",
                "ai_barberai_category_selected", "ai_caption_category_selected", "ai_celebratingideas_category_selected", "ai_chat_avatarai_catgory_selected", "ai_chat_btn_click",
                "ai_chat_business_catgory_selected", "ai_chat_caption_catgory_selected", "ai_chat_fun_catgory_selected", "ai_chat_generate_now_btn_click", "ai_chat_love_catgory_selected",
                "ai_chat_social_catgory_selected", "ai_chat_wallpaperai_catgory_selected", "ai_chat_work_catgory_selected", "ai_chat_writing_catgory_selected", "ai_common_category_selected",
                "ai_creator_btn_click", "ai_download_btn_click", "ai_facebook_share_btn", "ai_fashionai_category_selected", "ai_festival_retry_btn_click",
                "ai_festival_retry_popup_open", "ai_festival_template_edit_click", "ai_image_btn_click", "ai_image_generate_now_btn_click", "ai_image_regenerate_btn_click",
                "ai_image_save_jpg_pro_open", "ai_image_selected_share_screen", "ai_instagram_share_btn", "ai_interiorai_category_selected", "ai_invitation_retry_btn_click",
                "ai_invitation_retry_popup_open", "ai_invitation_template_edit_click", "ai_jewelleryai_category_selected", "ai_logo_category_selected",
                "ai_logo_subcategory_selected", "ai_logoai_category_selected", "ai_love_category_selected", "ai_main_screen_skip_btn_click", "ai_normal_festival_template_edit_click",
                "ai_normal_invitation_template_edit_click", "ai_others_category_selected", "ai_poster_edit_btn_click", "ai_poster_retry_btn_click",
                "ai_poster_retry_popup_open", "ai_ratio_selected_16_9", "ai_ratio_selected_1_1", "ai_ratio_selected_9_16", "ai_ratio_selected_portrait", "ai_ratio_selected_square",
                "ai_regenerate_btn_click", "ai_remove_watermark_one_time_btn_clicked", "ai_remove_watermark_pro_clicked", "ai_remove_watermark_pro_purchase_success", "ai_retry_btn_click",
                "ai_share_btn_click", "ai_sticker_category_selected", "ai_wallpaper_category_selected", "ai_wallpaperai_category_selected", "ai_wallpapper_category_selected",
                "ai_whatsapp_share_btn", "ai_work_category_selected", "align_btn", "alphabetic_element_btn", "ambedkarjayanti_element_btn",
                "animals_element_btn", "aprilfool_element_btn", "arrow_element_btn", "art_element_btn", "autofill_btn",
                "back_to_lobby_yes_btn", "barbie_element_btn", "bg_btn", "bg_choosecolor_btn", "bg_gradiant_btn",
                "bg_import_btn", "bg_pickcolor_btn", "bg_remove_btn", "bg_reset_btn", "bg_solid_btn",
                "birthday_element_btn", "boho_element_btn", "bookday_element_btn", "brush_element_btn", "bubbleshapefont_element_btn",
                "business_element_btn", "callout_element_btn", "cartoon_element_btn", "choose_color_btn", "christmas_element_btn",
                "circle_element_btn", "cloud_element_btn", "cnw_btn_click", "creative_element_btn", "cricket_element_btn",
                "cyberpunk_element_btn", "diwali_element_btn", "dont_losseoffer_subscribe_btn_click", "doodle_element_btn", "download_btn_click",
                "dp__content_edit_clicked", "dp_btn_click", "dp_cricket_content_edit_clicked", "dp_devotional_content_edit_clicked", "dp_festival_content_edit_clicked",
                "dp_friendshipday_content_edit_clicked", "dp_goodmorning_content_edit_clicked", "dp_goodthoughts_content_edit_clicked", "dp_independenceday_content_edit_clicked", "dp_janmashtami_content_edit_clicked",
                "dp_leadersquotes_content_edit_clicked", "dp_nagpanchami_content_edit_clicked", "dp_olympic2024_content_edit_clicked", "dp_rakshabandhan_content_edit_clicked", "dp_remove_watermark_btn_click",
                "dp_remove_watermark_one_time_btn_clicked", "dp_remove_watermark_popup_open", "dp_remove_watermark_pro_clicked", "dp_save_jpg_pro_open", "dp_shravanmass_content_edit_clicked",
                "draft_btn_click", "durgapooja_element_btn", "dussehra_element_btn", "earthday_element_btn", "easterday_element_btn",
                "editing_ai_chat_click", "editing_ai_chat_continuewrite", "editing_ai_chat_customtext", "editing_ai_chat_formal", "editing_ai_chat_improve",
                "editing_ai_chat_shorten", "editing_ai_image_click", "editing_ai_image_import", "editing_total_ai_chat_used", "editing_total_ai_image_used",
                "editor_screen_open", "education_element_btn", "effect_btn", "element_btn", "element_next_btn_click",
                "emoji_element_btn", "environmental_element_btn", "events_btn_click", "facebook_share_btn", "feather_element_btn",
                "feedback_editleave_close_without_submit", "feedback_editleave_open", "feedback_editleave_submit", "feedback_postediting_open", "feedback_postediting_submit",
                "festival_element_btn", "first_open", "fitness_element_btn", "fl_bikeevent_edit_btn_click", "fl_birthday_edit_btn_click",
                "fl_btn_click", "fl_business_edit_btn_click", "fl_camping_edit_btn_click", "fl_contest_edit_btn_click", "fl_cricket_edit_btn_click",
                "fl_educational_edit_btn_click", "fl_entertainment_edit_btn_click", "fl_fitness_edit_btn_click", "fl_food_drink_edit_btn_click", "fl_football_edit_btn_click",
                "fl_gettogether_edit_btn_click", "fl_hiring_edit_btn_click", "fl_inaugurations_edit_btn_click", "fl_lifestyle_edit_btn_click", "fl_newyearparty_edit_btn_click",
                "fl_productbranding_edit_btn_click", "fl_realestate_edit_btn_click", "fl_sale_edit_btn_click", "fl_salon_edit_btn_click", "fl_seminar_edit_btn_click",
                "fl_social_edit_btn_click", "fl_thanksgiving_edit_btn_click", "fl_travel_edit_btn_click", "flag_element_btn", "floral_element_btn",
                "font_btn", "football_element_btn", "frame_image_save_jpg_pro_open", "frame_remove_watermark_popup_open", "frame_remove_watermark_pro_clicked",
                "frames_element_btn", "friendshipday_element_btn", "ft_aprilfoolday_edit_btn_click", "ft_bhaidooj_edit_btn_click", "ft_btn_click",
                "ft_childrensday_edit_btn_click", "ft_christmas_edit_btn_click", "ft_columbusday_edit_btn_click", "ft_diwali_edit_btn_click", "ft_durgapooja_edit_btn_click",
                "ft_dussehra_edit_btn_click", "ft_earthday_edit_btn_click", "ft_easterday_edit_btn_click", "ft_electionsday_edit_btn_click", "ft_environmentday_edit_btn_click",
                "ft_friendshipday_edit_btn_click", "ft_ganeshchaturthi_edit_btn_click", "ft_goodfriday_edit_btn_click", "ft_gudipadwa_edit_btn_click", "ft_gurunanakjayanti_edit_btn_click",
                "ft_gurupurnima_edit_btn_click", "ft_halloween_edit_btn_click", "ft_holi_edit_btn_click", "ft_independenceday_edit_btn_click", "ft_janmashtami_edit_btn_click",
                "ft_kalichaudas_edit_btn_click", "ft_karwachauth_edit_btn_click", "ft_labhpancham_edit_btn_click", "ft_laborday_edit_btn_click", "ft_lohri_edit_btn_click",
                "ft_mahashivratri_edit_btn_click", "ft_makarsankranti_edit_btn_click", "ft_memorialday_edit_btn_click", "ft_micchamidukkadam_edit_btn_click", "ft_muharram_edit_btn_click",
                "ft_navratri_edit_btn_click", "ft_newyear_edit_btn_click", "ft_onam_edit_btn_click", "ft_patricksday_edit_btn_click", "ft_pongal_edit_btn_click",
                "ft_rakshabandhan_edit_btn_click", "ft_ramnavami_edit_btn_click", "ft_republicday_edit_btn_click", "ft_sharadpurnima_edit_btn_click", "ft_shravanmaas_edit_btn_click",
                "ft_shubhdhanteras_edit_btn_click", "ft_siblingsday_edit_btn_click", "ft_spring_edit_btn_click", "ft_teachersday_edit_btn_click", "ft_vaghbaras_edit_btn_click",
                "ft_valentinesday_edit_btn_click", "ft_vasantpanchami_edit_btn_click", "ft_veteransday_edit_btn_click", "ft_womensday_edit_btn_click", "ft_worldbookday_edit_btn_click",
                "ft_worldhealthday_edit_btn_click", "ft_worldmusicday_edit_btn_click", "ft_yogaday_edit_btn_click", "ft_youthday_edit_btn_click", "gandhijayanti_element_btn",
                "ganeshchaturthi_element_btn", "goodfriday_element_btn", "gradient_bg_btn", "grid_element_btn", "gudipadwa_element_btn",
                "halloween_element_btn", "handcraft_element_btn", "health_element_btn", "heart_element_btn", "hiring_element_btn",
                "holi_element_btn", "independenceday_element_btn", "invitation_edit_btn_click", "janmashtami_element_btn", "karwachauth_element_btn",
                "keyboard_btn", "krishna_element_btn", "ladder_shapefont_element_btn", "lagan_lagna_element_btn", "labor_element_btn",
                "line_element_btn", "linkedin_share_btn", "lohri_element_btn", "love_element_btn", "mahashivratri_element_btn",
                "makarsankranti_element_btn", "makarsankranti_offer_click", "makarsankranti_offer_continue", "makarsankranti_offer_open", "makarsankranti_offer_skip",
                "makarsankranti_offer_subscribe", "makarsankranti_offer_yes", "makarsankranti_offer_skip", "makarsankranti_offer_subscribe", "makarsankranti_offer_yes",
                "martinlutherkingday_element_btn", "memory_element_btn", "micchamidukkadam_element_btn", "music_element_btn", "nagpanchami_element_btn",
                "navratri_element_btn", "newyear_element_btn", "newyearparty_element_btn", "onam_element_btn", "others_element_btn",
                "pencil_element_btn", "photodoodle_element_btn", "pongal_element_btn", "polygon_element_btn", "poster_edit_btn_click",
                "productbranding_element_btn", "rakhabandhan_element_btn", "ramnavami_element_btn", "ramzan_element_btn", "realestate_element_btn",
                "rectangleshape_element_btn", "republicday_element_btn", "rocketshapefont_element_btn", "sale_element_btn", "sarcastic_element_btn",
                "savetriptap_btn", "scroll_element_btn", "sharadpurnima_element_btn", "shapes_btn", "shravanmass_element_btn",
                "shubhdhanteras_element_btn", "shubhalaganshape_element_btn", "siblingsday_element_btn", "spring_element_btn", "square_btn",
                "sticker_btn", "sun_element_btn", "summershape_element_btn", "thanksgiving_element_btn", "travel_element_btn",
                "tulip_element_btn", "twitter_share_btn", "vaghbaras_element_btn", "valentinesday_element_btn", "vasantpanchami_element_btn",
                "veteransday_element_btn", "victoryday_element_btn", "wall_element_btn", "whatsapp_share_btn", "womensday_element_btn",
                "worldbookday_element_btn", "worldhealthday_element_btn", "worldmusicday_element_btn", "yogaday_element_btn", "youthday_element_btn",
                "onboarding_start", "onboarding_complete", "onboarding_skip",
                "leaderboard_success", "social_share", "social_like", "social_comment", "social_follow", "social_unfollow", "social_message", "social_post",
                "social_story", "social_tag", "social_mention", "social_group_join", "social_group_leave", "social_group_create", "social_group_delete",
                "social_event_create", "social_event_update", "social_event_delete", "social_event_invite", "social_event_attend", "social_event_unattend",
                "social_event_share", "social_event_comment", "social_event_like", "social_event_reaction", "social_event_rating", "social_event_review",
                "social_event_feedback", "social_event_photo_upload", "social_event_video_upload", "social_event_link_share", "social_event_post",
                "social_event_story", "social_event_tag", "social_event_mention", "social_event_share_message", "social_event_share_comment", "social_event_share_reaction",
                "onboard_4th_screen_skip", "onboard_4th_screen_visible", "opacity_btn", "ornaments_element_btn", "paper_element_btn", "plastic_element_btn",
                "pongal_element_btn", "pro_screen_open", "profile_btn", "profile_btn_click", "profile_edit_btn", "profile_save_btn", "profile_upload_btn",
                "rakshabandhan_element_btn", "ramadan_element_btn", "ramnavmi_element_btn", "remove_watermark_btn_click", "remove_watermark_one_time_btn_clicked",
                "remove_watermark_popup_open", "remove_watermark_pro_clicked", "remove_watermark_pro_purchase_success", "replace_img_btn", "republicday_element_btn",
                "result_failed_time", "retro_element_btn", "retro_element_used", "reward_ad_show", "rotation_btn", "sale_element_btn", "save_as_darft_btn",
                "save_jpg_pro_ad_watched", "save_jpg_pro_buypro_clicked", "save_jpg_pro_open", "search_btn", "search_no_result_found", "shapes_element_btn",
                "share_screen_remove_watermark_btn_click", "share_screen_remove_watermark_popup_open", "siblingsday_element_btn", "size_btn", "sm_btn_click",
                "sm_facebookcovers_edit_btn_click", "sm_facebookpost_edit_btn_click", "sm_instagrampost_edit_btn_click", "sm_instagramstory_edit_btn_click",
                "sm_linkedinpost_edit_btn_click", "sm_photocollage_edit_btn_click", "sm_quotes_edit_btn_click", "sm_whatsappstatus_edit_btn_click",
                "sm_youtubebanner_edit_btn_click", "sm_youtubethumbnails_edit_btn_click", "socialmedia_element_btn", "solid_bg_btn", "space_btn",
                "sparkles_element_btn", "spiritual_element_btn", "sports_element_btn", "st_content_edit_btn_click", "stamp_element_btn",
                "step2_content_edit_screen_open", "support_btn_click", "tattoo_element_btn", "text_btn", "text_image_ai_btn_click", "tr_ai_chat_btn_click",
                "tr_ai_chat_business_catgory_selected", "tr_ai_chat_caption_catgory_selected", "tr_ai_chat_fun_catgory_selected", "tr_ai_chat_love_catgory_selected",
                "tr_ai_chat_social_catgory_selected", "tr_ai_chat_work_catgory_selected", "tr_ai_chat_writing_catgory_selected", "tr_ai_toggle_btn_click",
                "tr_btn_click", "tr_text_image_ai_btn_click", "travel_element_btn", "usa_element_btn", "valentinesday_element_btn", "vasantpanchami_element_btn",
                "vc_art_design_edit_btn_click", "vc_automobile_edit_btn_click", "vc_beauty_salon_edit_btn_click", "vc_btn_click", "vc_business_edit_btn_click",
                "vc_corporate_edit_btn_click", "vc_education_edit_btn_click", "vc_entertainmnet_edit_btn_click", "vc_eventplanner_edit_btn_click",
                "vc_fashion_edit_btn_click", "vc_fitness_edit_btn_click", "vc_food_edit_btn_click", "vc_homeservice_edit_btn_click", "vc_jewellery_edit_btn_click",
                "vc_lawyer_edit_btn_click", "vc_medical_edit_btn_click", "vc_photography_edit_btn_click", "vc_realestate_edit_btn_click", "vc_spa_massage_edit_btn_click",
                "vc_technology_edit_btn_click", "vc_travel_edit_btn_click", "vc_visitingcards_edit_btn_click", "watch_tutorial_btn", "wedding_element_btn",
                "whatsapp_share_btn", "womensday_element_btn", "youthday_element_btn", "zodiac_element_btn"

            ]



        matched_events_list = [
                "first_open","step1_homescreen_launched", "step2_content_edit_screen_open", "step3_content_saved"
            ]

            # Filter the main data to include only matched events for 'app_remove' users
        matched_events_df = app_remove_df[app_remove_df['event_name'].isin(matched_events_list)]


            # Define the labels based on event sequences
        def label_event_flow(events):
                unique_events = list(dict.fromkeys(events))  # Remove duplicates while preserving order
                if unique_events == ["first_open"]:
                    return "During Onboarding"
                elif unique_events == ["first_open", "step1_homescreen_launched"]:
                    return "After Launching Home Screen"
                elif unique_events == ["first_open", "step1_homescreen_launched", "step2_content_edit_screen_open"]:
                    return "After Entering Editing Mode"
                elif unique_events == ["first_open", "step1_homescreen_launched", "step2_content_edit_screen_open", "step3_content_saved"]:
                    return "After Content Save"
                else:
                    return "Other"

        # Group by user and collect events in sequence
        event_flow_df = matched_events_df.groupby('user_pseudo_id').apply(lambda x: x['event_name'].tolist()).reset_index()
        event_flow_df.columns = ['user_pseudo_id', 'event_sequence']
        event_flow_df = matched_events_df.groupby('user_pseudo_id').apply(lambda x: x['event_name'].tolist()).reset_index()
        event_flow_df.columns = ['user_pseudo_id', 'event_sequence']


            # Apply the labeling function
        event_flow_df['event_label'] = event_flow_df['event_sequence'].apply(label_event_flow)
        st.write("Event Flow for 'app_remove' Users with Matched Events and Labels:")
        st.dataframe(event_flow_df)


        matched_events_df = app_remove_df[app_remove_df['event_name'].isin(matched_events_list)]
        matched_events_df = matched_events_df.merge(event_flow_df[['user_pseudo_id', 'event_label']], on='user_pseudo_id', how='left')
        st.write("Event Flow for 'app_remove' Users with Matched Events and Categories:")
        st.dataframe(matched_events_df)

        last_5_records_df1 = last_5_records_df1.merge(event_flow_df[['user_pseudo_id', 'event_label']], on='user_pseudo_id', how='left')
        #st.write("Last 5 Valid Records for Users with 'app_remove' Event (excluding 'app_remove') with Event Labels:")
        #st.dataframe(last_5_records_df1)

        users_with_paid_ad = last_5_records_df1.groupby('user_pseudo_id').filter(lambda x: 'paid_ad_impression' in x['event_name'].values)

        # Create the pivot table grouped by 'event_label'
        pivot_table = users_with_paid_ad.groupby('event_label')['user_pseudo_id'].nunique().reset_index(name='Total users')

        # Sort the pivot table by the 'Total users' column in descending order
        pivot_table = pivot_table.sort_values(by='Total users', ascending=False)

        # Calculate the percentage of each event label
        pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100
        with col1:
        # Display the pivot table in Streamlit
            st.write("Pivot Table of app removed users last 5 record in paid ad impression:")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))



        pivot_table = matched_events_df.groupby('event_label').nunique()['user_pseudo_id'].reset_index(name='Total users')
        pivot_table = pivot_table.sort_values(by='Total users', ascending=False)
        pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100
        with col2:
            st.write("Pivot Table of app removed users flow:")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))

        matched_events_df = non_app_remove_df[non_app_remove_df['event_name'].isin(matched_events_list)]


        # Define the labels based on event sequences
        def label_event_flow(events):
                unique_events = list(dict.fromkeys(events))  # Remove duplicates while preserving order
                if unique_events == ["first_open"]:
                    return "During Onboarding"
                elif unique_events == ["first_open", "step1_homescreen_launched"]:
                    return "After Launching Home Screen"
                elif unique_events == ["first_open", "step1_homescreen_launched", "step2_content_edit_screen_open"]:
                    return "While Editing"
                elif unique_events == ["first_open", "step1_homescreen_launched", "step2_content_edit_screen_open", "step3_content_saved"]:
                    return "After Content Save"
                else:
                    return "Other"

            # Group by user and collect events in sequence
        event_flow_df = matched_events_df.groupby('user_pseudo_id').apply(lambda x: x['event_name'].tolist()).reset_index()
        event_flow_df.columns = ['user_pseudo_id', 'event_sequence']
        event_flow_df = matched_events_df.groupby('user_pseudo_id').apply(lambda x: x['event_name'].tolist()).reset_index()
        event_flow_df.columns = ['user_pseudo_id', 'event_sequence']


            # Apply the labeling function
        event_flow_df['event_label'] = event_flow_df['event_sequence'].apply(label_event_flow)
        st.write("Event Flow for 'churn' Users with Matched Events and Labels:")
        st.dataframe(event_flow_df)


        matched_events_df = non_app_remove_df[non_app_remove_df['event_name'].isin(matched_events_list)]
        matched_events_df = matched_events_df.merge(event_flow_df[['user_pseudo_id', 'event_label']], on='user_pseudo_id', how='left')
        #st.write("Event Flow for 'churn' Users with Matched Events and Categories:")
        #st.dataframe(matched_events_df)

        last_5_records_df2 = last_5_records_df2.merge(event_flow_df[['user_pseudo_id', 'event_label']], on='user_pseudo_id', how='left')
        st.write("Last 5 Valid Records for Users without 'app_remove' Event")
        st.dataframe(last_5_records_df2)

        pivot_table = matched_events_df.groupby('event_label').nunique()['user_pseudo_id'].reset_index(name='Total users')
        pivot_table = pivot_table.sort_values(by='Total users', ascending=False)
        pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100
        with col2:
            st.write("Pivot Table of Churn users flow:")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))

        users_with_paid_ad = last_5_records_df2.groupby('user_pseudo_id').filter(lambda x: 'paid_ad_impression' in x['event_name'].values)

        # Create the pivot table grouped by 'event_label'
        pivot_table = users_with_paid_ad.groupby('event_label')['user_pseudo_id'].nunique().reset_index(name='Total users')

        # Sort the pivot table by the 'Total users' column in descending order
        pivot_table = pivot_table.sort_values(by='Total users', ascending=False)

        # Calculate the percentage of each event label
        pivot_table['Percentage'] = (pivot_table['Total users'] / pivot_table['Total users'].sum()) * 100
        with col2:
        # Display the pivot table in Streamlit
            st.write("Pivot Table of Churn users last 5 record in paid ad impression :")
            st.write(pivot_table.style.format({'Percentage': "{:.2f}%"}))


if __name__ == "__main__":
    main()
