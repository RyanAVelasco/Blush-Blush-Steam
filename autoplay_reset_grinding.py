import os
import pyautogui
import time


screenX, screenY = pyautogui.size()
if screenX != 1920 and screenY != 1080:
    pyautogui.alert("Please set screen size to 1920x1080 before running script", "Incorrect Screen Size", "Quit")
    quit()


portraits = {
    #  Animal
    "animal_anon": os.path.join("images", "ui_icon_guys_animal_anon.png"),
    "animal_dmitri": os.path.join("images", "ui_icon_guys_animal_dmitri.png"),
    "animal_eli": os.path.join("images", "ui_icon_guys_animal_eli.png"),
    "animal_garret": os.path.join("images", "ui_icon_guys_animal_garret.png"),
    "animal_ichiban": os.path.join("images", "ui_icon_guys_animal_ichiban.png"),
    "animal_kelby": os.path.join("images", "ui_icon_guys_animal_kelby.png"),
    "animal_myx": os.path.join("images", "ui_icon_guys_animal_myx.png"),
    "animal_nimh": os.path.join("images", "ui_icon_guys_animal_nimh.png"),
    "animal_scale": os.path.join("images", "ui_icon_guys_animal_scale.png"),
    "animal_stirling": os.path.join("images", "ui_icon_guys_animal_stirling.png"),
    "animal_sven": os.path.join("images", "ui_icon_guys_animal_sven.png"),
    "animal_volks": os.path.join("images", "ui_icon_guys_animal_volks.png"),
    "animal_william": os.path.join("images", "ui_icon_guys_animal_william.png"),
    #  Demi-Human
    "demihuman_anon": os.path.join("images", "ui_icon_guys_demi-human_anon.png"),
    "demihuman_dmitri": os.path.join("images", "ui_icon_guys_demi-human_dmitri.png"),
    "demihuman_eli": os.path.join("images", "ui_icon_guys_demi-human_eli.png"),
    "demihuman_garret": os.path.join("images", "ui_icon_guys_demi-human_garret.png"),
    "demihuman_ichiban": os.path.join("images", "ui_icon_guys_demi-human_ichiban.png"),
    "demihuman_kelby": os.path.join("images", "ui_icon_guys_demi-human_kelby.png"),
    "demihuman_myx": os.path.join("images", "ui_icon_guys_demi-human_myx.png"),
    "demihuman_nimh": os.path.join("images", "ui_icon_guys_demi-human_nimh.png"),
    "demihuman_scale": os.path.join("images", "ui_icon_guys_demi-human_scale.png"),
    "demihuman_stirling": os.path.join("images", "ui_icon_guys_stirling.png"),
    "demihuman_sven": os.path.join("images", "ui_icon_guys_demi-human_sven.png"),
    "demihuman_volks": os.path.join("images", "ui_icon_guys_demi-human_volks.png"),
    "demihuman_william": os.path.join("images", "ui_icon_guys_demi-human_william.png"),
    #  Human
    "human_anon": os.path.join("images", "ui_icon_guys_human_anon.png"),
    "human_dmitri": os.path.join("images", "ui_icon_guys_human_dmitri.png"),
    "human_eli": os.path.join("images", "ui_icon_guys_human_eli.png"),
    "human_garret": os.path.join("images", "ui_icon_guys_human_garret.png"),
    "human_ichiban": os.path.join("images", "ui_icon_guys_human_ichiban.png"),
    "human_kelby": os.path.join("images", "ui_icon_guys_human_kelby.png"),
    "human_myx": os.path.join("images", "ui_icon_guys_human_myx.png"),
    "human_scale": os.path.join("images", "ui_icon_guys_human_scale.png"),
    "human_stirling": os.path.join("images", "ui_icon_guys_human_stirlingvolks.png"),
    "human_sven": os.path.join("images", "ui_icon_guys_human_sven.png"),
    "human_volks": os.path.join("images", "ui_icon_guys_human_volks.png"),
    "human_william": os.path.join("images", "ui_icon_guys_human_william.png"),
}

requirements = {
    #  NIMH
    "requirement_nimh_adversary": os.path.join("images", "ui_guys_req_adversary_nimh.png"),
    "requirement_nimh_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_nimh.png"),
    "requirement_nimh_frenemy": os.path.join("images", "ui_guys_req_frenemy_nimh.png"),
    "requirement_nimh_friendzone": os.path.join("images", "ui_guys_req_friendzone_nimh.png"),
    "requirement_nimh_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_nimh.png"),
    "requirement_nimh_crush": os.path.join("images", "ui_guys_req_crush_nimh.png"),
    "requirement_nimh_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_nimh.png"),
    "requirement_nimh_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_nimh.png"),
    "requirement_nimh_lover": os.path.join("images", "ui_guys_req_lover_nimh.png"),
    #  VOLKS
    "requirement_volks_adversary": os.path.join("images", "ui_guys_req_adversary_volks.png"),
    "requirement_volks_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_volks.png"),
    "requirement_volks_frenemy": os.path.join("images", "ui_guys_req_frenemy_volks.png"),
    "requirement_volks_friendzone": os.path.join("images", "ui_guys_req_friendzone_volks.png"),
    "requirement_volks_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_volks.png"),
    "requirement_volks_crush": os.path.join("images", "ui_guys_req_crush_volks.png"),
    "requirement_volks_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_volks.png"),
    "requirement_volks_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_volks.png"),
    "requirement_volks_lover": os.path.join("images", "ui_guys_req_lover_volks.png"),
    #  KELBY
    "requirement_kelby_adversary": os.path.join("images", "ui_guys_req_adversary_kelby.png"),
    "requirement_kelby_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_kelby.png"),
    "requirement_kelby_frenemy": os.path.join("images", "ui_guys_req_frenemy_kelby.png"),
    "requirement_kelby_friendzone": os.path.join("images", "ui_guys_req_friendzone_kelby.png"),
    "requirement_kelby_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_kelby.png"),
    "requirement_kelby_crush": os.path.join("images", "ui_guys_req_crush_kelby.png"),
    "requirement_kelby_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_kelby.png"),
    "requirement_kelby_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_kelby.png"),
    "requirement_kelby_lover": os.path.join("images", "ui_guys_req_lover_kelby.png"),
    #  ELI
    "requirement_eli_adversary": os.path.join("images", "ui_guys_req_adversary_eli.png"),
    "requirement_eli_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_eli.png"),
    "requirement_eli_frenemy": os.path.join("images", "ui_guys_req_frenemy_eli.png"),
    "requirement_eli_friendzone": os.path.join("images", "ui_guys_req_friendzone_eli.png"),
    "requirement_eli_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_eli.png"),
    "requirement_eli_crush": os.path.join("images", "ui_guys_req_crush_eli.png"),
    "requirement_eli_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_eli.png"),
    "requirement_eli_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_eli.png"),
    "requirement_eli_lover": os.path.join("images", "ui_guys_req_lover_eli.png"),
    #  ANON
    "requirement_anon_adversary": os.path.join("images", "ui_guys_req_adversary_anon.png"),
    "requirement_anon_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_anon.png"),
    "requirement_anon_frenemy": os.path.join("images", "ui_guys_req_frenemy_anon.png"),
    "requirement_anon_friendzone": os.path.join("images", "ui_guys_req_friendzone_anon.png"),
    "requirement_anon_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_anon.png"),
    "requirement_anon_crush": os.path.join("images", "ui_guys_req_crush_anon.png"),
    "requirement_anon_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_anon.png"),
    "requirement_anon_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_anon.png"),
    "requirement_anon_lover": os.path.join("images", "ui_guys_req_lover_anon.png"),
    #  GARRET
    "requirement_garret_adversary": os.path.join("images", "ui_guys_req_adversary_garret.png"),
    "requirement_garret_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_garret.png"),
    "requirement_garret_frenemy": os.path.join("images", "ui_guys_req_frenemy_garret.png"),
    "requirement_garret_friendzone": os.path.join("images", "ui_guys_req_friendzone_garret.png"),
    "requirement_garret_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_garret.png"),
    "requirement_garret_crush": os.path.join("images", "ui_guys_req_crush_garret.png"),
    "requirement_garret_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_garret.png"),
    "requirement_garret_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_garret.png"),
    "requirement_garret_lover": os.path.join("images", "ui_guys_req_lover_garret.png"),
    #  DMITRI
    "requirement_dmitri_adversary": os.path.join("images", "ui_guys_req_adversary_dmitri.png"),
    "requirement_dmitri_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_dmitri.png"),
    "requirement_dmitri_frenemy": os.path.join("images", "ui_guys_req_frenemy_dmitri.png"),
    "requirement_dmitri_friendzone": os.path.join("images", "ui_guys_req_friendzone_dmitri.png"),
    "requirement_dmitri_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_dmitri.png"),
    "requirement_dmitri_crush": os.path.join("images", "ui_guys_req_crush_dmitri.png"),
    "requirement_dmitri_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_dmitri.png"),
    "requirement_dmitri_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_dmitri.png"),
    "requirement_dmitri_lover": os.path.join("images", "ui_guys_req_lover_dmitri.png"),
    #  ICHIBAN
    "requirement_ichiban_adversary": os.path.join("images", "ui_guys_req_adversary_ichiban.png"),
    "requirement_ichiban_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_ichiban.png"),
    "requirement_ichiban_frenemy": os.path.join("images", "ui_guys_req_frenemy_ichiban.png"),
    "requirement_ichiban_friendzone": os.path.join("images", "ui_guys_req_friendzone_ichiban.png"),
    "requirement_ichiban_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_ichiban.png"),
    "requirement_ichiban_crush": os.path.join("images", "ui_guys_req_crush_ichiban.png"),
    "requirement_ichiban_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_ichiban.png"),
    "requirement_ichiban_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_ichiban.png"),
    "requirement_ichiban_lover": os.path.join("images", "ui_guys_req_lover_ichiban.png"),
    #  WILLIAM
    "requirement_william_adversary": os.path.join("images", "ui_guys_req_adversary_william.png"),
    "requirement_william_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_william.png"),
    "requirement_william_frenemy": os.path.join("images", "ui_guys_req_frenemy_william.png"),
    "requirement_william_friendzone": os.path.join("images", "ui_guys_req_friendzone_william.png"),
    "requirement_william_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_william.png"),
    "requirement_william_crush": os.path.join("images", "ui_guys_req_crush_william.png"),
    "requirement_william_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_william.png"),
    "requirement_william_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_william.png"),
    "requirement_william_lover": os.path.join("images", "ui_guys_req_lover_william.png"),
    #  MYX
    "requirement_myx_adversary": os.path.join("images", "ui_guys_req_adversary_myx.png"),
    "requirement_myx_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_myx.png"),
    "requirement_myx_frenemy": os.path.join("images", "ui_guys_req_frenemy_myx.png"),
    "requirement_myx_friendzone": os.path.join("images", "ui_guys_req_friendzone_myx.png"),
    "requirement_myx_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_myx.png"),
    "requirement_myx_crush": os.path.join("images", "ui_guys_req_crush_myx.png"),
    "requirement_myx_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_myx.png"),
    "requirement_myx_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_myx.png"),
    "requirement_myx_lover": os.path.join("images", "ui_guys_req_lover_myx.png"),
    #  SCALE
    "requirement_scale_adversary": os.path.join("images", "ui_guys_req_adversary_scale.png"),
    "requirement_scale_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_scale.png"),
    "requirement_scale_frenemy": os.path.join("images", "ui_guys_req_frenemy_scale.png"),
    "requirement_scale_friendzone": os.path.join("images", "ui_guys_req_friendzone_scale.png"),
    "requirement_scale_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_scale.png"),
    "requirement_scale_crush": os.path.join("images", "ui_guys_req_crush_scale.png"),
    "requirement_scale_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_scale.png"),
    "requirement_scale_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_scale.png"),
    "requirement_scale_lover": os.path.join("images", "ui_guys_req_lover_scale.png"),
    #  STIRLING
    "requirement_stirling_adversary": os.path.join("images", "ui_guys_req_adversary_stirling.png"),
    "requirement_stirling_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_stirling.png"),
    "requirement_stirling_frenemy": os.path.join("images", "ui_guys_req_frenemy_stirling.png"),
    "requirement_stirling_friendzone": os.path.join("images", "ui_guys_req_friendzone_stirling.png"),
    "requirement_stirling_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_stirling.png"),
    "requirement_stirling_crush": os.path.join("images", "ui_guys_req_crush_stirling.png"),
    "requirement_stirling_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_stirling.png"),
    "requirement_stirling_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_stirling.png"),
    "requirement_stirling_lover": os.path.join("images", "ui_guys_req_lover_stirling.png"),
    #  SVEN
    "requirement_sven_adversary": os.path.join("images", "ui_guys_req_adversary_sven.png"),
    "requirement_sven_acquaintance": os.path.join("images", "ui_guys_req_acquaintance_sven.png"),
    "requirement_sven_frenemy": os.path.join("images", "ui_guys_req_frenemy_sven.png"),
    "requirement_sven_friendzone": os.path.join("images", "ui_guys_req_friendzone_sven.png"),
    "requirement_sven_awkward_besties": os.path.join("images", "ui_guys_req_awkward_besties_sven.png"),
    "requirement_sven_crush": os.path.join("images", "ui_guys_req_crush_sven.png"),
    "requirement_sven_sweetheart": os.path.join("images", "ui_guys_req_sweetheart_sven.png"),
    "requirement_sven_boyfriend": os.path.join("images", "ui_guys_req_boyfriend_sven.png"),
    "requirement_sven_lover": os.path.join("images", "ui_guys_req_lover_sven.png")

}

gift = {
    #  Buttons
    "gift-button": os.path.join("images", "ui_icon_guys_gift.png"),
    "pay-button": os.path.join("images", "ui_icon_pay.png"),
    "buy-more": os.path.join("images", "ui_icon_gift_more.png"),
    "buy-less": os.path.join("images", "ui_icon_gift_less.png"),
    "page-up": os.path.join("images", "ui_icon_gift_page_up.png"),
    #  Reference
    "quantity-1": os.path.join("images", "ui_icon_gift_count_1.png"),
    "quantity-5": os.path.join("images", "ui_icon_gift_count_5.png"),
    "quantity-10": os.path.join("images", "ui_icon_gift_count_10.png"),
    "quantity-25": os.path.join("images", "ui_icon_gift_count_25.png"),
    "quantity-50": os.path.join("images", "ui_icon_gift_count_50.png"),
    "quantity-100": os.path.join("images", "ui_icon_gift_count_100.png"),
    "quantity-1k": os.path.join("images", "ui_icon_gift_count_1K.png"),
    "quantity-10k": os.path.join("images", "ui_icon_gift_count_10K.png"),
    "quantity-100k": os.path.join("images", "ui_icon_gift_count_100K.png"),
    "quantity-1m": os.path.join("images", "ui_icon_gift_count_1M.png"),
    "animal_page_1": os.path.join("images", "ui_icon_gift_animal_page-1-of-3.png"),
    "animal_page_2": os.path.join("images", "ui_icon_gift_animal_page-2-of-3.png"),
    "animal_page_3": os.path.join("images", "ui_icon_gift_animal_page-3-of-3.png"),
    "demi_human_human_page_1": os.path.join("images", "ui_icon_gift_demi-human-human_page-1-of-3.png"),
    "demi_human_human_page_2": os.path.join("images", "ui_icon_gift_demi-human-human_page-2-of-3.png"),
    "demi_human_human_page_3": os.path.join("images", "ui_icon_gift_demi-human-human_page-3-of-3.png"),
    #  Gifts
    "apples": os.path.join("images", "ui_icon_gift_apple.png"),
    "ball": os.path.join("images", "ui_icon_gift_ball.png"),
    "blanket": os.path.join("images", "ui_icon_gift_blanket.png"),
    "bone": os.path.join("images", "ui_icon_gift_bone.png"),
    "boxers": os.path.join("images", "ui_icon_gift_boxers.png"),
    "calculator": os.path.join("images", "ui_icon_gift_calculator.png"),
    "coffee": os.path.join("images", "ui_icon_gift_coffee.png"),
    "collar": os.path.join("images", "ui_icon_gift_collar.png"),
    "cologne": os.path.join("images", "ui_icon_gift_cologne.png"),
    "comb": os.path.join("images", "ui_icon_gift_comb.png"),
    "dishwasher": os.path.join("images", "ui_icon_gift_dishwasher.png"),
    "drone": os.path.join("images", "ui_icon_gift_drone.png"),
    "encyclopedia": os.path.join("images", "ui_icon_gift_encyclopedia.png"),
    "fountain": os.path.join("images", "ui_icon_gift_fountain.png"),
    "games": os.path.join("images", "ui_icon_gift_games.png"),
    "hammock": os.path.join("images", "ui_icon_gift_hammock.png"),
    "headphones": os.path.join("images", "ui_icon_gift_headphones.png"),
    "heatlamp": os.path.join("images", "ui_icon_gift_heatlamp.png"),
    "herb": os.path.join("images", "ui_icon_gift_herb.png"),
    "ice-cream": os.path.join("images", "ui_icon_gift_ice-cream.png"),
    "jet": os.path.join("images", "ui_icon_gift_jet.png"),
    "laptop": os.path.join("images", "ui_icon_gift_laptop.png"),
    "laser": os.path.join("images", "ui_icon_gift_laser.png"),
    "laundry": os.path.join("images", "ui_icon_gift_laundry.png"),
    "lint-roller": os.path.join("images", "ui_icon_gift_lint-roller.png"),
    "loafers": os.path.join("images", "ui_icon_gift_loafers.png"),
    "neck-pillow": os.path.join("images", "ui_icon_gift_neck-pillow.png"),
    "newspaper": os.path.join("images", "ui_icon_gift_newspaper.png"),
    "piano": os.path.join("images", "ui_icon_gift_piano.png"),
    "pie": os.path.join("images", "ui_icon_gift_pie.png"),
    "pillow": os.path.join("images", "ui_icon_gift_pillow.png"),
    "pizza": os.path.join("images", "ui_icon_gift_pizza.png"),
    "scratcher": os.path.join("images", "ui_icon_gift_scratcher.png"),
    "seeds": os.path.join("images", "ui_icon_gift_seeds.png"),
    "shampoo": os.path.join("images", "ui_icon_gift_shampoo.png"),
    "socks": os.path.join("images", "ui_icon_gift_socks.png"),
    "sunglasses": os.path.join("images", "ui_icon_gift_sunglasses.png"),
    "ticket": os.path.join("images", "ui_icon_gift_ticket.png"),
    "tools": os.path.join("images", "ui_icon_gift_tools.png"),
    "toy": os.path.join("images", "ui_icon_gift_toy.png"),
    "tree": os.path.join("images", "ui_icon_gift_tree.png"),
    "tuna-can": os.path.join("images", "ui_icon_gift_tuna-can.png"),
    "vacuum": os.path.join("images", "ui_icon_gift_vacuum.png"),
    "veggie-tray": os.path.join("images", "ui_icon_gift_veggie-tray.png"),
    "watch": os.path.join("images", "ui_icon_gift_watch.png")
}

date = {
    "boat-ride": os.path.join("images", "ui_icon_date_boat-ride.png"),
    "carnival": os.path.join("images", "ui_icon_date_carnival.png"),
    "coaster": os.path.join("images", "ui_icon_date_coaster.png"),
    "dinner": os.path.join("images", "ui_icon_date_dinner.png"),
    "masquerade": os.path.join("images", "ui_icon_date_masquerade.png")
}

icon = {
    #  UI
    "ui-guys": os.path.join("images", "ui_icon_guys.png"),
    "ui-jobs": os.path.join("images", "ui_icon_jobs.png"),
    "ui-hobbies": os.path.join("images", "ui_icon_hobbies.png"),
    "ui-stats": os.path.join("images", "ui_icon_stats.png"),
    #  guys
    "guys-buy-more": os.path.join("images", "ui_icon_guys_talk.png"),
    "guys-date": os.path.join("images", "ui_icon_guys_date.png"),
    "guys-gift": os.path.join("images", "ui_icon_guys_gift.png"),
    "guys-stats": os.path.join("images", "ui_icon_guys_stats.png"),
    "guys-talk": os.path.join("images", "ui_icon_guys_talk.png"),
    "guys-advance": os.path.join("images", "ui_icon_advance_relationship.png"),
    "guys-scrollbar": os.path.join("images", "ui_icon_guys_scrollbar.png"),
    #  jobs
    # "jobs-seamstress-on": os.path.join("images", "ui_icon_jobs_seamstress_active.png"),
    # "jobs-seamstress-off": os.path.join("images", "ui_icon_jobs_seamstress_inactive.png"),
    # "jobs-musician-on": os.path.join("images", "ui_icon_jobs_musician_active.png"),
    # "jobs-musician-off": os.path.join("images", "ui_icon_jobs_musician_inactive.png"),
    # "jobs-baker-on": os.path.join("images", "ui_icon_jobs_baker_active.png"),
    # "jobs-baker-off": os.path.join("images", "ui_icon_jobs_baker_inactive.png"),
    # "jobs-maid-on": os.path.join("images", "ui_icon_jobs_maid_active.png"),
    # "jobs-maid-off": os.path.join("images", "ui_icon_jobs_maid_inactive.png"),
    #  hobbies
    "hobbies-smart-on": os.path.join("images", "ui_icon_hobbies_smart_active.png"),
    "hobbies-smart-off": os.path.join("images", "ui_icon_hobbies_smart_inactive.png"),
    "hobbies-guts-on": os.path.join("images", "ui_icon_hobbies_guts_active.png"),
    "hobbies-guts-off": os.path.join("images", "ui_icon_hobbies_guts_inactive.png"),
    "hobbies-healthy-on": os.path.join("images", "ui_icon_hobbies_healthy_active.png"),
    "hobbies-healthy-off": os.path.join("images", "ui_icon_hobbies_healthy_inactive.png"),
    "hobbies-outgoing-on": os.path.join("images", "ui_icon_hobbies_outgoing_active.png"),
    "hobbies-outgoing-off": os.path.join("images", "ui_icon_hobbies_outgoing_inactive.png"),
    "hobbies-gamer-on": os.path.join("images", "ui_icon_hobbies_gamer_active.png"),
    "hobbies-gamer-off": os.path.join("images", "ui_icon_hobbies_gamer_inactive.png"),
    "hobbies-caring-on": os.path.join("images", "ui_icon_hobbies_caring_active.png"),
    "hobbies-caring-off": os.path.join("images", "ui_icon_hobbies_caring_inactive.png"),
    "hobbies-passionate-on": os.path.join("images", "ui_icon_hobbies_passionate_active.png"),
    "hobbies-passionate-off": os.path.join("images", "ui_icon_hobbies_passionate_inactive.png"),
    "hobbies-confidence-on": os.path.join("images", "ui_icon_hobbies_confidence_active.png"),
    "hobbies-confidence-off": os.path.join("images", "ui_icon_hobbies_confidence_inactive.png"),
    "hobbies-peaceful-on": os.path.join("images", "ui_icon_hobbies_peaceful_active.png"),
    "hobbies-peaceful-off": os.path.join("images", "ui_icon_hobbies_peaceful_inactive.png"),
    "hobbies-creative-on": os.path.join("images", "ui_icon_hobbies_creative_active.png"),
    "hobbies-creative-off": os.path.join("images", "ui_icon_hobbies_creative_inactive.png"),
    "hobbies-disciplined-on": os.path.join("images", "ui_icon_hobbies_disciplined_active.png"),
    "hobbies-disciplined-off": os.path.join("images", "ui_icon_hobbies_disciplined_inactive.png"),
    "hobbies-observant-on": os.path.join("images", "ui_icon_hobbies_observant_active.png"),
    "hobbies-observant-off": os.path.join("images", "ui_icon_hobbies_observant_inactive.png"),
    #  dates
    "dates-dinner": os.path.join("images", "ui_icon_date_dinner.png"),
    "dates-boat-ride": os.path.join("images", "ui_icon_date_boat-ride.png"),
    "dates-coaster": os.path.join("images", "ui_icon_date_coaster.png"),
    "dates-carnival": os.path.join("images", "ui_icon_date_carnival.png"),
    "dates-masquerade": os.path.join("images", "ui_icon_date_masquerade.png"),
    "dates-pay": os.path.join("images", "ui_icon_pay.png"),
    "date-go-again": os.path.join("images", "ui_icon_guys_date_go-again.png"),
    "date-complete": os.path.join("images", "ui_icon_guys_date_continue.png"),
    #  stats
    "soft_reset": os.path.join("images", "ui_icon_stats_reset.png"),
    "soft_reset_confirmation": os.path.join("images", "ui_stats_soft_reset_confirmation.png"),
    "soft_reset_ok": os.path.join("images", "ui_stats_soft_reset_confirmation_ok.png"),
    #  loading screens
    "loading_screen_1": os.path.join("images", "_loading_screen_1.png"),
    "loading_screen_2": os.path.join("images", "_loading_screen_2.png")
}

coordinates = {
    #  ui
    "ui-guys": (129, 927, 234, 153),
    "ui-jobs": (363, 927, 234, 153),
    "ui-hobbies": (602, 927, 234, 153),
    "ui-stats": (845, 927, 234, 153),
    #  guys
    "guys-buy-more": (1182, 562, 52, 53),
    "guys-date": (1078, 525, 150, 71),
    "guys-gift": (1068, 447, 166, 81),
    "guys-stats": (1068, 372, 166, 81),
    "guys-talk": (1071, 297, 166, 81),
    "okay": (1736, 844),
    "guys-scrollbar-position": (440, 292, 29, 593),
    "guys-nimh-scrollbar-position": (442, 311),
    "guys-volks-scrollbar-position": (442, 311),
    "guys-kelby-scrollbar-position": (442, 311),
    "guys-eli-scrollbar-position": (442, 436),
    "guys-anon-scrollbar-position": (442, 436),
    "guys-garret-scrollbar-position": (442, 436),
    "guys-dmitri-scrollbar-position": (442, 556),
    "guys-ichiban-scrollbar-position": (442, 556),
    "guys-william-scrollbar-position": (442, 556),
    "guys-myx-scrollbar-position": (442, 681),
    "guys-stirling-scrollbar-position": (442, 681),
    "guys-scale-scrollbar-position": (442, 681),
    "guys-sven-scrollbar-position": (442, 718),
    #  date
    "date-complete": (268, 717, 1378, 120),
    #  gift
    "gift-amount": (919, 540, 338, 100),
    #  jobs/hobbies
    "jobs_hobbies": (510, 310, 1248, 545),
    "jobs_seamstress": (647, 353),
    "jobs_musician": (1702, 353),
    "jobs_baker": (1076, 455),
    "jobs_maid": (1687, 455),
    "jobs_nurse": (1084, 572),
    "jobs_coffee-barista": (1699, 572),
    "jobs_teacher": (1083, 689),
    "jobs_streamer": (1698, 689),
    "jobs_writer": (1088, 429),
    "jobs_pit-mechanic": (1687, 430),
    "jobs_politician": (1077, 538),
    "jobs_pharmacist": (1699, 538),
    "jobs_florist": (1080, 664),
    "jobs_cryptominer": (1702, 664),
    "jobs_fundraiser": (1084, 780),
    "jobs_farmer": (1708, 780),
    #  requirements
    "requirements": (495, 281, 588, 601),
    #  misc
    "date_options": (501, 291, 569, 589),
    "date_pay_money": (1269, 470, 221, 105),
    "date_pay_gems": (1269, 634, 221, 105),
    "scrollbar_top_position": (1753, 337),
    "scrollbar_bottom_position": (1752, 837),
    "advance": (1715, 831),
    "soft_reset": (1238, 729, 179, 50),
    "soft_reset_confirmation": (424, 242, 1068, 574),
    "soft_reset_ok": (1007, 690, 209, 74),
    "loading_screen_1": (654, 293, 601, 526),
    "loading_screen_2": (428, 321, 1077, 460)
}

#  Toggles
#  Jobs
SEAMSTRESS = False
MUSICIAN = False
BAKER = False
MAID = False
NURSE = False
COFFEE_BARISTA = False
TEACHER = False
STREAMER = False
WRITER = False
PIT_MECHANIC = False
POLITICIAN = False
PHARMACIST = False
FLORIST = False
CRYPTOMINER = False
FUNDRAISER = False
FARMER = False
#   Hobbies
SMART = False
GUTS = False
HEALTHY = False
OUTGOING = False
GAMER = False
CARING = False
PASSIONATE = False
CONFIDENCE = False
PEACEFUL = False
CREATIVE = False
DISCIPLINED = False
OBSERVANT = False


def guy_toggle(name, type):
    getpos = pyautogui.locateOnScreen(icon["guys-scrollbar"],
                                      region=coordinates["guys-scrollbar-position"],
                                      confidence=0.95,
                                      grayscale=True)
    if type == "animal":
        if name == "nimh":
            x, y = coordinates["guys-nimh-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_nimh"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "volks":
            x, y = coordinates["guys-volks-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_volks"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "kelby":
            x, y = coordinates["guys-kelby-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_kelby"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "eli":
            x, y = coordinates["guys-eli-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_eli"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "anon":
            x, y = coordinates["guys-anon-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_anon"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "garret":
            x, y = coordinates["guys-garret-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_garret"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "dmitri":
            x, y = coordinates["guys-dmitri-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_dmitri"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "ichiban":
            x, y = coordinates["guys-ichiban-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_ibchiban"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "william":
            x, y = coordinates["guys-william-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_william"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "myx":
            x, y = coordinates["guys-myx-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_myx"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "stirling":
            x, y = coordinates["guys-stirling-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_stirling"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "scale":
            x, y = coordinates["guys-scale-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_scale"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "sven":
            x, y = coordinates["guys-sven-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["animal_sven"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
    elif type == "demihuman":
        if name == "nimh":
            x, y = coordinates["guys-nimh-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_nimh"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "volks":
            x, y = coordinates["guys-volks-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_volks"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "kelby":
            x, y = coordinates["guys-kelby-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_kelby"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "eli":
            x, y = coordinates["guys-eli-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_eli"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "anon":
            x, y = coordinates["guys-anon-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_anon"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "garret":
            x, y = coordinates["guys-garret-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_garret"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "dmitri":
            x, y = coordinates["guys-dmitri-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_dmitri"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "ichiban":
            x, y = coordinates["guys-ichiban-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_ibchiban"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "william":
            x, y = coordinates["guys-william-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_william"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "myx":
            x, y = coordinates["guys-myx-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_myx"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "stirling":
            x, y = coordinates["guys-stirling-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_stirling"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "scale":
            x, y = coordinates["guys-scale-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_scale"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "sven":
            x, y = coordinates["guys-sven-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["demihuman_sven"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
    elif type == "human":
        if name == "nimh":
            x, y = coordinates["guys-nimh-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_nimh"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "volks":
            x, y = coordinates["guys-volks-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_volks"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "kelby":
            x, y = coordinates["guys-kelby-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_kelby"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "eli":
            x, y = coordinates["guys-eli-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_eli"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "anon":
            x, y = coordinates["guys-anon-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_anon"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "garret":
            x, y = coordinates["guys-garret-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_garret"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "dmitri":
            x, y = coordinates["guys-dmitri-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_dmitri"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "ichiban":
            x, y = coordinates["guys-ichiban-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_ibchiban"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "william":
            x, y = coordinates["guys-william-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_william"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "myx":
            x, y = coordinates["guys-myx-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_myx"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "stirling":
            x, y = coordinates["guys-stirling-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_stirling"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "scale":
            x, y = coordinates["guys-scale-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_scale"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))
        elif name == "sven":
            x, y = coordinates["guys-sven-scrollbar-position"]
            pyautogui.moveTo(getpos)
            pyautogui.mouseDown(button="left")
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button="left")
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateOnScreen(portraits["human_sven"],
                                                     region=(124, 286, 360, 604),
                                                     confidence=0.9))


def job_toggle(job, toggle):
    global SEAMSTRESS
    global MUSICIAN
    global BAKER
    global MAID
    global NURSE
    global COFFEE_BARISTA
    global TEACHER
    global STREAMER
    global WRITER
    global PIT_MECHANIC
    global POLITICIAN
    global PHARMACIST
    global FLORIST
    global CRYPTOMINER
    global FUNDRAISER
    global FARMER

    if job == "seamstress":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("up")
        pyautogui.click(coordinates["jobs_seamstress"])
        if toggle == "on":
            SEAMSTRESS = True
        elif toggle == "off":
            SEAMSTRESS = False

    elif job == "musician":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("up")
        pyautogui.click(coordinates["jobs_musician"])
        if toggle == "on":
            MUSICIAN = True
        elif toggle == "off":
            MUSICIAN = False

    elif job == "baker":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("up")
        pyautogui.click(coordinates["jobs_baker"])
        if toggle == "on":
            BAKER = True
        elif toggle == "off":
            BAKER = False

    elif job == "maid":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("up")
        pyautogui.click(coordinates["jobs_maid"])
        if toggle == "on":
            MAID = True
        elif toggle == "off":
            MAID = False

    elif job == "nurse":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("up")
        pyautogui.click(coordinates["jobs_nurse"])
        if toggle == "on":
            NURSE = True
        elif toggle == "off":
            NURSE = False

    elif job == "coffee-barista":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("up")
        pyautogui.click(coordinates["jobs_coffee-barista"])
        if toggle == "on":
            COFFEE_BARISTA = True
        elif toggle == "off":
            COFFEE_BARISTA = False

    elif job == "teacher":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("up")
        pyautogui.click(coordinates["jobs_teacher"])
        if toggle == "on":
            TEACHER = True
        elif toggle == "off":
            TEACHER = False

    elif job == "streamer":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("up")
        pyautogui.click(coordinates["jobs_streamer"])
        if toggle == "on":
            STREAMER = True
        elif toggle == "off":
            STREAMER = False

    elif job == "writer":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("down")
        pyautogui.click(coordinates["jobs_writer"])
        if toggle == "on":
            WRITER = True
        elif toggle == "off":
            WRITER = False

    elif job == "pit-mechanic":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("down")
        pyautogui.click(coordinates["jobs_pit-mechanic"])
        if toggle == "on":
            PIT_MECHANIC = True
        elif toggle == "off":
            PIT_MECHANIC = False

    elif job == "politician":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("down")
        pyautogui.click(coordinates["jobs_politician"])
        if toggle == "on":
            POLITICIAN = True
        elif toggle == "off":
            POLITICIAN = False

    elif job == "pharmacist":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("down")
        pyautogui.click(coordinates["jobs_pharmacist"])
        if toggle == "on":
            PHARMACIST = True
        elif toggle == "off":
            PHARMACIST = False

    elif job == "florist":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("down")
        pyautogui.click(coordinates["jobs_florist"])
        if toggle == "on":
            FLORIST = True
        elif toggle == "off":
            FLORIST = False

    elif job == "cryptominer":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("down")
        pyautogui.click(coordinates["jobs_cryptominer"])
        if toggle == "on":
            CRYPTOMINER = True
        elif toggle == "off":
            CRYPTOMINER = False

    elif job == "fundraiser":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("down")
        pyautogui.click(coordinates["jobs_fundraiser"])
        if toggle == "on":
            FUNDRAISER = True
        elif toggle == "off":
            FUNDRAISER = False

    elif job == "farmer":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-jobs"],
                                                 region=coordinates["ui-jobs"],
                                                 grayscale=True,
                                                 confidence=0.95))
        time.sleep(0.5)
        drag("down")
        pyautogui.click(coordinates["jobs_farmer"])
        if toggle == "on":
            FARMER = True
        elif toggle == "off":
            FARMER = False


def hobby_toggle(hobbies, switch):
    global SMART
    global GUTS
    global HEALTHY
    global OUTGOING
    global GAMER
    global CARING
    global PASSIONATE
    global CONFIDENCE
    global PEACEFUL
    global CREATIVE
    global DISCIPLINED
    global OBSERVANT

    loopcut = False
    if hobbies == "smart" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-smart-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-smart-off"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        SMART = True
        time.sleep(0.1)

    elif hobbies == "smart" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-smart-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-smart-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        SMART = False
        time.sleep(0.1)

    elif hobbies == "guts" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-guts-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-guts-off"],
                                                         grayscale=True))
                loopcut = True
        GUTS = True
        time.sleep(0.1)

    elif hobbies == "guts" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-guts-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-guts-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        GUTS = False
        time.sleep(0.1)

    elif hobbies == "healthy" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-healthy-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-healthy-off"],
                                                         grayscale=True))
                loopcut = True
        HEALTHY = True
        time.sleep(0.1)

    elif hobbies == "healthy" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-healthy-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-healthy-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        HEALTHY = False
        time.sleep(0.1)

    elif hobbies == "outgoing" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-outgoing-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-outgoing-off"],
                                                         grayscale=True))
                loopcut = True
        OUTGOING = True
        time.sleep(0.1)

    elif hobbies == "outgoing" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-outgoing-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-outgoing-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        GAMER = False
        time.sleep(0.1)

    elif hobbies == "gamer" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-gamer-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-gamer-off"],
                                                         grayscale=True))
                loopcut = True
        GAMER = True
        time.sleep(0.1)

    elif hobbies == "gamer" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-gamer-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-gamer-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        OUTGOING = False
        time.sleep(0.1)

    elif hobbies == "caring" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-caring-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-caring-off"],
                                                         grayscale=True))
                loopcut = True
        CARING = True
        time.sleep(0.1)

    elif hobbies == "caring" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-caring-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-caring-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        CARING = False
        time.sleep(0.1)

    elif hobbies == "passionate" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-passionate-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-passionate-off"],
                                                         grayscale=True))
                loopcut = True
        PASSIONATE = True
        time.sleep(0.1)

    elif hobbies == "passionate" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-passionate-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-passionate-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        PASSIONATE = False
        time.sleep(0.1)

    elif hobbies == "confidence" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-confidence-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-confidence-off"],
                                                         grayscale=True))
                loopcut = True
        CONFIDENCE = True
        time.sleep(0.1)

    elif hobbies == "confidence" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-confidence-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-confidence-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        CONFIDENCE = False
        time.sleep(0.1)

    elif hobbies == "peaceful" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-peaceful-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-peaceful-off"],
                                                         grayscale=True))
                loopcut = True
        PEACEFUL = True
        time.sleep(0.1)

    elif hobbies == "peaceful" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-peaceful-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-peaceful-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        PEACEFUL = False
        time.sleep(0.1)

    elif hobbies == "creative" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-creative-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-creative-off"],
                                                         grayscale=True))
                loopcut = True
        CREATIVE = True
        time.sleep(0.1)

    elif hobbies == "creative" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-creative-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-creative-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        CREATIVE = False
        time.sleep(0.1)

    elif hobbies == "disciplined" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-disciplined-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-disciplined-off"],
                                                         grayscale=True))
                loopcut = True
        DISCIPLINED = True
        time.sleep(0.1)

    elif hobbies == "disciplined" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-disciplined-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-disciplined-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        DISCIPLINED = False
        time.sleep(0.1)

    elif hobbies == "observant" and switch == "on":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-observant-on"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-observant-off"],
                                                         grayscale=True))
                loopcut = True
        OBSERVANT = True
        time.sleep(0.1)

    elif hobbies == "observant" and switch == "off":
        pyautogui.click(pyautogui.locateOnScreen(icon["ui-hobbies"],
                                                 region=coordinates["ui-hobbies"],
                                                 grayscale=True))
        time.sleep(2)
        if not pyautogui.locateOnScreen(icon["hobbies-observant-off"],
                                        region=coordinates["jobs_hobbies"],
                                        grayscale=True):
            while loopcut is False:
                pyautogui.click(pyautogui.locateOnScreen(icon["hobbies-observant-on"],
                                                         region=coordinates["jobs_hobbies"],
                                                         grayscale=True))
                loopcut = True
        OBSERVANT = False
        time.sleep(0.1)


def dating(dates, count):
    loopcut = False
    cycle = 0
    paid = False
    if dates == "dinner":
        pyautogui.click(pyautogui.locateOnScreen(icon["guys-date"]))
        time.sleep(0.5)
        while loopcut is False:
            if pyautogui.locateOnScreen(date["dinner"]):
                pyautogui.click(pyautogui.locateOnScreen(date["dinner"],
                                                         region=coordinates["date_options"],
                                                         grayscale=True))
                while paid is False and cycle < count:
                    if pyautogui.locateOnScreen(icon["dates-pay"],
                                                             region=coordinates["date_pay_money"],
                                                             grayscale=True):
                        pyautogui.click(pyautogui.locateOnScreen(icon["dates-pay"],
                                                                 region=coordinates["date_pay_money"],
                                                                 grayscale=True))
                        paid = True
                while cycle != count:
                    if pyautogui.locateOnScreen(icon["date-complete"]):
                        pyautogui.click(pyautogui.locateOnScreen(icon["date-go-again"],
                                                                 region=coordinates["date-complete"],
                                                                 grayscale=True))
                        cycle += 1
                    continue
                time.sleep(0.25)
                pyautogui.click(pyautogui.locateOnScreen(icon["date-complete"],
                                                         region=coordinates["date-complete"],
                                                         grayscale=True))
                loopcut = True

    elif dates == "boat-ride":
        pyautogui.click(pyautogui.locateOnScreen(icon["guys-date"]))
        time.sleep(0.5)
        while loopcut is False:
            if pyautogui.locateOnScreen(date["boat-ride"]):
                pyautogui.click(pyautogui.locateOnScreen(date["boat-ride"],
                                                         region=coordinates["date_options"],
                                                         grayscale=True))
                while paid is False and cycle < count:
                    if pyautogui.locateOnScreen(icon["dates-pay"],
                                                             region=coordinates["date_pay_money"],
                                                             grayscale=True):
                        pyautogui.click(pyautogui.locateOnScreen(icon["dates-pay"],
                                                                 region=coordinates["date_pay_money"],
                                                                 grayscale=True))
                        paid = True
                while cycle != count:
                    if pyautogui.locateOnScreen(icon["date-complete"]):
                        pyautogui.click(pyautogui.locateOnScreen(icon["date-go-again"],
                                                                 region=coordinates["date-complete"],
                                                                 grayscale=True))
                        cycle += 1
                    continue
                time.sleep(0.25)
                pyautogui.click(pyautogui.locateOnScreen(icon["date-complete"],
                                                         region=coordinates["date-complete"],
                                                         grayscale=True))
                loopcut = True

    elif dates == "coaster":
        pyautogui.click(pyautogui.locateOnScreen(icon["guys-date"]))
        time.sleep(0.5)
        while loopcut is False:
            if pyautogui.locateOnScreen(date["coaster"]):
                pyautogui.click(pyautogui.locateOnScreen(date["coaster"],
                                                         region=coordinates["date_options"],
                                                         grayscale=True))
                while paid is False and cycle < count:
                    if pyautogui.locateOnScreen(icon["dates-pay"],
                                                             region=coordinates["date_pay_money"],
                                                             grayscale=True):
                        pyautogui.click(pyautogui.locateOnScreen(icon["dates-pay"],
                                                                 region=coordinates["date_pay_money"],
                                                                 grayscale=True))
                        paid = True
                while cycle != count:
                    if pyautogui.locateOnScreen(icon["date-complete"]):
                        pyautogui.click(pyautogui.locateOnScreen(icon["date-go-again"],
                                                                 region=coordinates["date-complete"],
                                                                 grayscale=True))
                        cycle += 1
                    continue
                time.sleep(0.25)
                pyautogui.click(pyautogui.locateOnScreen(icon["date-complete"],
                                                         region=coordinates["date-complete"],
                                                         grayscale=True))
                loopcut = True

    elif dates == "carnival":
        pyautogui.click(pyautogui.locateOnScreen(icon["guys-date"]))
        time.sleep(0.5)
        while loopcut is False:
            if pyautogui.locateOnScreen(date["carnival"]):
                pyautogui.click(pyautogui.locateOnScreen(date["carnival"],
                                                         region=coordinates["date_options"],
                                                         grayscale=True))
                while paid is False and cycle != count:
                    if pyautogui.locateOnScreen(icon["dates-pay"],
                                                             region=coordinates["date_pay_money"],
                                                             grayscale=True):
                        pyautogui.click(pyautogui.locateOnScreen(icon["dates-pay"],
                                                                 region=coordinates["date_pay_money"],
                                                                 grayscale=True))
                        paid = True
                while cycle != count:
                    if pyautogui.locateOnScreen(icon["date-complete"]):
                        pyautogui.click(pyautogui.locateOnScreen(icon["date-go-again"],
                                                                 region=coordinates["date-complete"],
                                                                 grayscale=True))
                        cycle += 1
                    continue
                time.sleep(0.25)
                pyautogui.click(pyautogui.locateOnScreen(icon["date-complete"],
                                                         region=coordinates["date-complete"],
                                                         grayscale=True))
                loopcut = True

    elif dates == "masquerade":
        pyautogui.click(pyautogui.locateOnScreen(icon["guys-date"]))
        time.sleep(0.5)
        pyautogui.moveTo(940, 540)
        while loopcut is False:
            if pyautogui.locateOnScreen(date["masquerade"]):
                pyautogui.click(pyautogui.locateOnScreen(date["masquerade"],
                                                         region=coordinates["date_options"],
                                                         grayscale=True))
                while paid is False and cycle < count:
                    if pyautogui.locateOnScreen(icon["dates-pay"],
                                                             region=coordinates["date_pay_money"],
                                                             grayscale=True):
                        pyautogui.click(pyautogui.locateOnScreen(icon["dates-pay"],
                                                                 region=coordinates["date_pay_money"],
                                                                 grayscale=True))
                        paid = True
                while cycle != count:
                    if pyautogui.locateOnScreen(icon["date-complete"]):
                        pyautogui.click(pyautogui.locateOnScreen(icon["date-go-again"],
                                                                 region=coordinates["date-complete"],
                                                                 grayscale=True))
                        cycle += 1
                    continue
                time.sleep(0.25)
                pyautogui.click(pyautogui.locateOnScreen(icon["date-complete"],
                                                         region=coordinates["date-complete"],
                                                         grayscale=True))
                loopcut = True
            else:
                pyautogui.scroll(-50)



def gifting(gifts, page, count):
    loopcut = False
    paid = False
    pyautogui.click(pyautogui.locateOnScreen(icon["guys-gift"],
                                             region=coordinates["guys-gift"],
                                             grayscale=True))

    if page == 2:
        pyautogui.click(pyautogui.locateOnScreen(gift["page-up"]))
    elif page == 3:
        pyautogui.click(pyautogui.locateOnScreen(gift["page-up"]))
        time.sleep(0.5)
        pyautogui.click(pyautogui.locateOnScreen(gift["page-up"]))

    time.sleep(0.5)
    while loopcut is False:
        #  animal gifts page 1
        if gifts == "apples":
            if pyautogui.locateOnScreen(gift["animal_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["apples"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "newspaper":
            if pyautogui.locateOnScreen(gift["animal_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["newspaper"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "seeds":
            if pyautogui.locateOnScreen(gift["animal_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["seeds"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "veggie-tray":
            if pyautogui.locateOnScreen(gift["animal_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["veggie-tray"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "tuna-can":
            if pyautogui.locateOnScreen(gift["animal_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["tuna-can"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "comb":
            if pyautogui.locateOnScreen(gift["animal_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["comb"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "herb":
            if pyautogui.locateOnScreen(gift["animal_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["herb"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "lint-roller":
            if pyautogui.locateOnScreen(gift["animal_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["lint-roller"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True

        #  animal gifts page 2
        if gifts == "toy":
            if pyautogui.locateOnScreen(gift["animal_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["toy"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "pillow":
            if pyautogui.locateOnScreen(gift["animal_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["pillow"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "heatlamp":
            if pyautogui.locateOnScreen(gift["animal_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["heatlamp"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "fountain":
            if pyautogui.locateOnScreen(gift["animal_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["fountain"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "hammock":
            if pyautogui.locateOnScreen(gift["animal_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["hammock"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "scratcher":
            if pyautogui.locateOnScreen(gift["animal_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["scratcher"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "laser":
            if pyautogui.locateOnScreen(gift["animal_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["laser"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "collar":
            if pyautogui.locateOnScreen(gift["animal_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["collar"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True

        #  animal gifts page 3
        if gifts == "blanket":
            if pyautogui.locateOnScreen(gift["animal_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["blanket"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "shampoo":
            if pyautogui.locateOnScreen(gift["animal_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["shampoo"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "loafers":
            if pyautogui.locateOnScreen(gift["animal_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["loafers"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "ball":
            if pyautogui.locateOnScreen(gift["animal_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["ball"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "tree":
            if pyautogui.locateOnScreen(gift["animal_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["tree"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "bone":
            if pyautogui.locateOnScreen(gift["animal_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["bone"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "boxers":
            if pyautogui.locateOnScreen(gift["animal_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["boxers"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True

        #  demi-human/human gifts page 1
        if gifts == "coffee":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["coffee"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "pizza":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["pizza"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "ice-cream":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["ice-cream"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "socks":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["socks"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "pie":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["pie"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "calculator":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["calculator"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
                    time.sleep(0.5)
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            time.sleep(0.5)
            loopcut = True
        if gifts == "sunglasses":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["sunglasses"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "neck-pillow":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_1"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["neck-pillow"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True

        #  demi-human/human gifts page 2
        if gifts == "tools":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["tools"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True,
                                                         confidence=0.9))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "watch":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["watch"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "drone":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["drone"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "ticket":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["ticket"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "games":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["games"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "cologne":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["cologne"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "vacuum":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["vacuum"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "encyclopedia":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_2"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["encyclopedia"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True

        #  demi-human/human gifts page 3
        if gifts == "headphones":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["headphones"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "laptop":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["laptop"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "piano":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["piano"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "dishwasher":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["dishwasher"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "laundry":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["laundry"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "jet":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["jet"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True
        if gifts == "boxers":
            if pyautogui.locateOnScreen(gift["demi_human_human_page_3"]):
                pyautogui.click(pyautogui.locateOnScreen(gift["boxers"],
                                                         region=coordinates["requirements"],
                                                         grayscale=True))
                while not pyautogui.locateOnScreen(count):
                    pyautogui.click(pyautogui.locateOnScreen(gift["buy-more"],
                                                             region=coordinates["gift-amount"],
                                                             grayscale=True))
            while paid is False:
                if pyautogui.locateOnScreen(gift["pay-button"]):
                    pyautogui.click(pyautogui.locateOnScreen(gift["pay-button"]), button="left")
                    paid = True
            loopcut = True


def drag(move):
    if move == "up":
        pyautogui.moveTo(coordinates["scrollbar_bottom_position"])
        pyautogui.mouseDown(button="left")
        pyautogui.moveTo(1752, 337)
        pyautogui.mouseUp(button="left")
    elif move == "down":
        pyautogui.moveTo(coordinates["scrollbar_top_position"])
        pyautogui.mouseDown(button="left")
        pyautogui.moveTo(1752, 837)
        pyautogui.mouseUp(button="left")


def advance_relationship():
    pyautogui.doubleClick(1715, 831, interval=0.25, button="left")


def soft_reset():
    global SEAMSTRESS
    global MUSICIAN
    global BAKER
    global MAID
    global NURSE
    global COFFEE_BARISTA
    global TEACHER
    global STREAMER
    global WRITER
    global PIT_MECHANIC
    global POLITICIAN
    global PHARMACIST
    global FLORIST
    global CRYPTOMINER
    global FUNDRAISER
    global FARMER
    global SMART
    global GUTS
    global HEALTHY
    global OUTGOING
    global GAMER
    global CARING
    global PASSIONATE
    global CONFIDENCE
    global PEACEFUL
    global CREATIVE
    global DISCIPLINED
    global OBSERVANT

    pyautogui.click(pyautogui.locateOnScreen(icon["ui-stats"],
                                             region=coordinates["ui-stats"],
                                             grayscale=True))
    while not pyautogui.locateOnScreen(icon["soft_reset"]):
        continue
    pyautogui.click(pyautogui.locateOnScreen(icon["soft_reset"]))
    while not pyautogui.locateOnScreen(icon["soft_reset_confirmation"],
                                       region=coordinates["soft_reset_confirmation"],
                                       grayscale=True):
        continue
    pyautogui.click(pyautogui.locateOnScreen(icon["soft_reset_ok"],
                                             region=coordinates["soft_reset_ok"],
                                             grayscale=True))

    SEAMSTRESS = False
    MUSICIAN = False
    BAKER = False
    MAID = False
    NURSE = False
    COFFEE_BARISTA = False
    TEACHER = False
    STREAMER = False
    WRITER = False
    PIT_MECHANIC = False
    POLITICIAN = False
    PHARMACIST = False
    FLORIST = False
    CRYPTOMINER = False
    FUNDRAISER = False
    FARMER = False
    SMART = False
    GUTS = False
    HEALTHY = False
    OUTGOING = False
    GAMER = False
    CARING = False
    PASSIONATE = False
    CONFIDENCE = False
    PEACEFUL = False
    CREATIVE = False
    DISCIPLINED = False
    OBSERVANT = False

    while not pyautogui.locateOnScreen(icon["loading_screen_1"],
                                       region=coordinates["loading_screen_1"],
                                       grayscale=True):
        continue

    while not pyautogui.locateOnScreen(icon["loading_screen_2"],
                                       region=coordinates["loading_screen_2"],
                                       grayscale=True):
        continue

    while pyautogui.locateOnScreen(icon["loading_screen_2"],
                                   region=coordinates["loading_screen_2"],
                                   grayscale=True):
        continue


game = True

while game is True:
    reset = False
    while reset is False:
        print(time.asctime(time.localtime(time.time())))
        # Nimh: Adversary to Acquaintance
        while not pyautogui.locateOnScreen(requirements["requirement_nimh_adversary"],
                                           region=coordinates["requirements"],
                                           grayscale=True):
            if SEAMSTRESS is False:
                job_toggle("seamstress", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))
            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Nimh: Acquaintance to Frenemy
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_nimh_acquaintance"],
                                           region=coordinates["requirements"],
                                           grayscale=True):
            while date_check is True:
                dating("dinner", 1)
                date_check = False

            if SMART is False:
                while SMART is False:
                    hobby_toggle("smart", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Nimh: Frenemy to Friendzone
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_nimh_frenemy"],
                                           region=coordinates["requirements"],
                                           grayscale=True):
            while date_check is True:
                dating("boat-ride", 1)
                date_check = False

            while gift_check is True:
                gifting("seeds", 1, gift["quantity-1"])
                gift_check = False

            if GUTS is False:
                while GUTS is False:
                    hobby_toggle("guts", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))
            if MUSICIAN is False:
                while MUSICIAN is False:
                    job_toggle("musician", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
            time.sleep(.5)
        advance_relationship()

        # Nimh: Friendzone to Awkward Besties
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_nimh_friendzone"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("coaster", 1)
                date_check = False

            while gift_check is True:
                gifting("veggie-tray", 1, gift["quantity-1"])
                gift_check = False

            if HEALTHY is False:
                while HEALTHY is False:
                    hobby_toggle("healthy", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            while BAKER is False or \
                MAID is False:
                job_toggle("baker", "on")
                job_toggle("maid", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))

            time.sleep(.5)
        advance_relationship()

        # Nimh: Awkward Besties to Crush
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_nimh_awkward_besties"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 1)
                date_check = False

            while OUTGOING is False or \
                    CARING is False:
                hobby_toggle("outgoing", "on")
                hobby_toggle("caring", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))
            if NURSE is False:
                while NURSE is False:
                    job_toggle("nurse", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Nimh: Crush to Sweetheart
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_nimh_crush"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("boat-ride", 1)
                date_check = False

            while gift_check is True:
                time.sleep(1)
                gifting("ice-cream", 1, gift["quantity-10"])
                gift_check = False

            if PASSIONATE is False:
                while PASSIONATE is False:
                    hobby_toggle("passionate", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Nimh: Sweetheart to Boyfriend
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_nimh_sweetheart"],
                                           region=coordinates["requirements"],
                                           grayscale=True):
            while date_check is True:
                dating("coaster", 1)
                date_check = False

            while gift_check is True:
                time.sleep(1)
                gifting("pie", 1, gift["quantity-1"])
                time.sleep(1)
                gifting("pie", 1, gift["quantity-1"])
                gift_check = False

            if SMART is False:
                while SMART is False:
                    hobby_toggle("smart", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))
            if GAMER is False:
                while GAMER is False:
                    hobby_toggle("gamer", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        guy_toggle("anon", "animal")
        time.sleep(0.5)

        # # Anon: Adversary to Acquaintance
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_anon_adversary"],
                                           region=coordinates["requirements"],
                                           grayscale=True):
            while date_check is True:
                dating("dinner", 15)
                date_check = False

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # # Anon: Acquaintance to Frenemy
        date_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_anon_acquaintance"],
                                           region=coordinates["requirements"],
                                           grayscale=True):
            while date_check is True:
                dating("boat-ride", 15)
                date_check = False

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Anon Frenemy to Friendzone
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_anon_frenemy"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while gift_check is True:
                gifting("hammock", 2, gift["quantity-50"])
                time.sleep(1)
                gifting("hammock", 2, gift["quantity-25"])
                gift_check = False

            while TEACHER is False or \
                    SEAMSTRESS is True or \
                    NURSE is True or \
                    MAID is True:
                job_toggle("teacher", "on")
                job_toggle("maid", "off")
                job_toggle("seamstress", "off")
                job_toggle("nurse", "off")

            pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                     region=coordinates["ui-guys"],
                                                     grayscale=True))
            while GAMER is False or \
                    SMART is False or \
                    DISCIPLINED is False or \
                    CONFIDENCE is False or \
                    PEACEFUL is False or \
                    CREATIVE is False:
                hobby_toggle("gamer", "on")
                hobby_toggle("smart", "on")
                hobby_toggle("disciplined", "on")
                hobby_toggle("confidence", "on")
                hobby_toggle("peaceful", "on")
                hobby_toggle("creative", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Anon Friendzone to Awkward Besties
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_anon_friendzone"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("carnival", 15)
                date_check = False

            while gift_check is True:
                gifting("tree", 3, gift["quantity-1"])
                gift_check = False

            # while TEACHER is True:
            #     job_toggle("teacher", "off")
            #     pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
            #                                              region=coordinates["ui-guys"],
            #                                              grayscale=True))

            while OBSERVANT is False:
                hobby_toggle("observant", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Anon Awkward Besties to Crush
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_anon_awkward_besties"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 15)
                date_check = False

            while gift_check is True:
                gifting("coffee", 1, gift["quantity-10k"])
                gift_check = False

            while TEACHER is False:
                job_toggle("teacher", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        guy_toggle("volks", "animal")
        time.sleep(0.5)

        # Volks Adversary to Acquaintance
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_volks_adversary"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 2)
                date_check = False

            if GUTS is False:
                while GUTS is False:
                    hobby_toggle("guts", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Volks Acquaintance to Frenemy
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_volks_acquaintance"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("boat-ride", 2)
                date_check = False

            if GUTS is False or \
                    HEALTHY is False:
                while GUTS is False:
                    hobby_toggle("guts", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))
                while HEALTHY is False:
                    hobby_toggle("healthy", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Volks Frenemy to Friendzone
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_volks_frenemy"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("coaster", 3)
                date_check = False

            while gift_check is True:
                gifting("lint-roller", 1, gift["quantity-1"])
                gift_check = False

            if SMART is False:
                while SMART is False:
                    hobby_toggle("smart", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Volks Friendzone to Awkward Besties
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_volks_friendzone"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("carnival", 3)
                date_check = False

            while gift_check is True:
                gifting("veggie-tray", 1, gift["quantity-10"])
                gift_check = False

            if GUTS is False:
                while GUTS is False:
                    hobby_toggle("guts", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Volks Awkward Besties to Crush
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_volks_awkward_besties"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 6)
                date_check = False
                time.sleep(1)

            while gift_check is True:
                gifting("coffee", 1, gift["quantity-5"])
                gift_check = False

            if CONFIDENCE is False:
                while CONFIDENCE is False:
                    hobby_toggle("confidence", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Volks Crush to Sweetheart
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_volks_crush"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("boat-ride", 5)
                date_check = False

            while gift_check is True:
                gifting("socks", 1, gift["quantity-1"])
                gift_check = False

            if OUTGOING is False:
                while OUTGOING is False:
                    hobby_toggle("outgoing", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Volks Sweetheart to Boyfriend
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_volks_sweetheart"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("coaster", 3)
                date_check = False

            while gift_check is True:
                gifting("sunglasses", 1, gift["quantity-1"])
                gift_check = False


            while BAKER is True:
                job_toggle("baker", "off")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            if SMART is False:
                while SMART is False:
                    hobby_toggle("smart", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        guy_toggle("kelby", "animal")
        time.sleep(0.5)

        # Kelby Adversary to Acquaintance
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_kelby_adversary"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 6)
                date_check = False

            if HEALTHY is False:
                while HEALTHY is False:
                    hobby_toggle("healthy", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Kelby Acquaintance to Frenemy
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_kelby_acquaintance"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("boat-ride", 6)
                date_check = False

            while HEALTHY is False or \
                    SMART is False:
                if HEALTHY is False:
                    hobby_toggle("healthy", "on")
                elif SMART is False:
                    hobby_toggle("smart", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Kelby Frenemy to Friendzone
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_kelby_frenemy"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("coaster", 6)
                date_check = False

            while gift_check is True:
                gifting("herb", 1, gift["quantity-10"])
                time.sleep(1)
                gifting("herb", 1, gift["quantity-5"])
                gift_check = False

            if OUTGOING is False:
                hobby_toggle("outgoing", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Kelby Friendzone to Awkward Bestites
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_kelby_friendzone"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("carnival", 6)
                date_check = False

            while gift_check is True:
                gifting("seeds", 1, gift["quantity-10k"])
                gift_check = False

            if GAMER is False:
                hobby_toggle("gamer", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        guy_toggle("eli", "animal")
        time.sleep(0.5)

        # Eli Adversary to Acquaintance
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_eli_adversary"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 10)
                date_check = False

            if OUTGOING is False:
                while OUTGOING is False:
                    hobby_toggle("outgoing", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Eli Acquaintance to Frenemy
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_eli_acquaintance"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("boat-ride", 10)
                date_check = False

            if CREATIVE is False or \
                    CONFIDENCE is False:
                hobby_toggle("creative", "on")
                hobby_toggle("confidence", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Eli Acquaintance to Frenemy
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_eli_frenemy"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("coaster", 10)
                date_check = False

            while gift_check is True:
                gifting("laser", 2, gift["quantity-1"])
                gift_check = False

            if PASSIONATE is False:
                hobby_toggle("passionate", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Eli Friendzone to Crush
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_eli_friendzone"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("carnival", 10)
                date_check = False

            while gift_check is True:
                gifting("hammock", 2, gift["quantity-50"])
                gift_check = False

            if HEALTHY is False:
                hobby_toggle("healthy", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        guy_toggle("garret", "animal")
        time.sleep(0.5)

        # Garret Adversary to Acquaintance
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_garret_adversary"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 20)
                date_check = False

            while WRITER is False:
                job_toggle("writer", "on")
                pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                         region=coordinates["ui-guys"],
                                                         grayscale=True))


            if CARING is False or \
                CONFIDENCE is False:
                    hobby_toggle("caring", "on")
                    hobby_toggle("confidence", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()
        guy_toggle("volks", "demihuman")
        time.sleep(0.5)

        # Volks Boyfriend to Lover
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_volks_boyfriend"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("carnival", 3)
                date_check = False

            while gift_check is True:
                gifting("tools", 2, gift["quantity-1"])
                gift_check = False

            if DISCIPLINED is False:
                while DISCIPLINED is False:
                    hobby_toggle("disciplined", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()
        guy_toggle("kelby", "demihuman")
        time.sleep(0.5)

        # Kelby Awkward Besties to Crush
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_kelby_awkward_besties"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 6)
                date_check = False

            while gift_check is True:
                gifting("sunglasses", 1, gift["quantity-1"])
                gift_check = False

            if DISCIPLINED is False:
                while DISCIPLINED is False:
                    hobby_toggle("disciplined", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()
        guy_toggle("eli", "demihuman")
        time.sleep(0.5)

        # Eli Awkward Besties to Crush
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_eli_awkward_besties"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 10)
                date_check = False

            while gift_check is True:
                gifting("pizza", 1, gift["quantity-1k"])
                time.sleep(1.5)
                gifting("pizza", 1, gift["quantity-1"])
                gift_check = False

            if OUTGOING is False:
                while OUTGOING is False:
                    hobby_toggle("outgoing", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()
        guy_toggle("anon", "demihuman")
        time.sleep(0.5)

        # Anon Crush to Sweetheart
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_anon_crush"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("boat-ride", 15)
                date_check = False

            while gift_check is True:
                #  bug where it refused to click the pay button unless I chose gift["quantity-100"]
                gifting("calculator", 1, gift["quantity-100"])

                #  original 3 lines of code below > Start
                # gifting("calculator", 1, gift["quantity-50"])
                # gifting("calculator", 1, gift["quantity-10"])
                # gifting("calculator", 1, gift["quantity-10"])
                #  original 3 lines of code below > End

                gift_check = False

            if GAMER is False:
                while GAMER is False:
                    hobby_toggle("gamer", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()
        guy_toggle("garret", "animal")
        time.sleep(0.5)

        # Garret Acquaintance to Frenemy
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_garret_acquaintance"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("boat-ride", 20)
                date_check = False

            if HEALTHY is False or \
                    PEACEFUL is False:
                while HEALTHY is False or \
                        PEACEFUL is False:
                    hobby_toggle("healthy", "on")
                    hobby_toggle("peaceful", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Garret Frenemy to Friendzone
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_garret_frenemy"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("coaster", 20)
                date_check = False

            if GUTS is False or \
                    CREATIVE is False:
                while GUTS is False or \
                        CREATIVE is False:
                    hobby_toggle("guts", "on")
                    hobby_toggle("creative", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Garret Friendzone to Awkward Besties
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_garret_friendzone"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("carnival", 20)
                date_check = False

            if CONFIDENCE is False or \
                    OUTGOING is False:
                while CONFIDENCE is False or \
                        OUTGOING is False:
                    hobby_toggle("guts", "on")
                    hobby_toggle("creative", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Garret Awkward Besties to Crush
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_garret_awkward_besties"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 20)
                date_check = False

            if PASSIONATE is False or \
                    OBSERVANT is False:
                while PASSIONATE is False or \
                        OBSERVANT is False:
                    hobby_toggle("passionate", "on")
                    hobby_toggle("observant", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()
        guy_toggle("nimh", "demihuman")
        time.sleep(0.5)

        # Nimh Boyfriend to Lover
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_nimh_boyfriend"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("carnival", 1)
                date_check = False

            while gift_check is True:
                gifting("calculator", 1, gift["quantity-1"])
                time.sleep(1.5)
                gifting("calculator", 1, gift["quantity-1"])
                gift_check = False

            if CARING is False:
                while CARING is False:
                    hobby_toggle("caring", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()

        # Nimh Lover to Lover + 1
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_nimh_lover"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("masquerade", 1)
                date_check = False

            while gift_check is True:
                gifting("neck-pillow", 1, gift["quantity-1"])
                gift_check = False

            if CREATIVE is False:
                while CREATIVE is False:
                    hobby_toggle("creative", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()
        guy_toggle("eli", "demihuman")
        time.sleep(0.5)

        # Eli Crush to Sweetheart
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_eli_crush"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("boat-ride", 10)
                date_check = False

            while gift_check is True:
                # gifting("pie", 1, gift["quantity-1k"])
                #  bug: refuses to perform the next lines starting at 2nd reset
                gifting("pie", 1, gift["quantity-100"])
                time.sleep(3)
                gifting("pie", 1, gift["quantity-100"])
                time.sleep(3)
                gifting("pie", 1, gift["quantity-100"])
                time.sleep(3)
                gifting("pie", 1, gift["quantity-10"])
                time.sleep(3)
                gifting("pie", 1, gift["quantity-5"])
                time.sleep(3)
                gift_check = False

            if GAMER is False:
                while GAMER is False:
                    hobby_toggle("gamer", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()
        guy_toggle("dmitri", "animal")
        time.sleep(0.5)

        # Dmitri Adversary to Acquaintance
        date_check = True
        gift_check = True
        while not pyautogui.locateOnScreen(requirements["requirement_dmitri_adversary"],
                                           region=coordinates["requirements"],
                                           grayscale=True):

            while date_check is True:
                dating("dinner", 25)
                date_check = False

            if PASSIONATE is False:
                while PASSIONATE is False:
                    hobby_toggle("passionate", "on")
                    pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
                                                             region=coordinates["ui-guys"],
                                                             grayscale=True))

            pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
                                                     region=coordinates["guys-talk"],
                                                     grayscale=True))
        advance_relationship()
        # guy_toggle("garret", "demihuman")
        # time.sleep(0.5)
        #
        # #  takes too long to reach lv31 PEACEFUL/SMART > 1 Minute
        # # Garret Crush to Sweetheart
        # date_check = True
        # gift_check = True
        # while not pyautogui.locateOnScreen(requirements["requirement_garret_crush"],
        #                                    region=coordinates["requirements"],
        #                                    grayscale=True):
        #
        #     while date_check is True:
        #         dating("boat-ride", 20)
        #         date_check = False
        #
        #     if PEACEFUL is False or \
        #             SMART is False:
        #         while PEACEFUL is False or \
        #                 SMART is False:
        #             hobby_toggle("peaceful", "on")
        #             hobby_toggle("smart", "on")
        #             pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
        #                                                      region=coordinates["ui-guys"],
        #                                                      grayscale=True))
        #
        #     pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
        #                                              region=coordinates["guys-talk"],
        #                                              grayscale=True))
        # advance_relationship()
        #
        # # Garett Sweetheart to Boyfriend
        # date_check = True
        # gift_check = True
        # while not pyautogui.locateOnScreen(requirements["requirement_garret_sweetheart"],
        #                                    region=coordinates["requirements"],
        #                                    grayscale=True):
        #
        #     while date_check is True:
        #         dating("coaster", 20)
        #         date_check = False
        #
        #     if HEALTHY is False or \
        #             DISCIPLINED is False:
        #         while HEALTHY is False or \
        #                 DISCIPLINED is False:
        #             hobby_toggle("healthy", "on")
        #             hobby_toggle("disciplined", "on")
        #             pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
        #                                                      region=coordinates["ui-guys"],
        #                                                      grayscale=True))
        #
        #     pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
        #                                              region=coordinates["guys-talk"],
        #                                              grayscale=True))
        # advance_relationship()
        # guy_toggle("volks", "human")
        # time.sleep(0.5)
        #
        # # Volks Lover to Lover + 1
        # date_check = True
        # gift_check = True
        # while not pyautogui.locateOnScreen(requirements["requirement_volks_lover"],
        #                                    region=coordinates["requirements"],
        #                                    grayscale=True):
        #
        #     while date_check is True:
        #         dating("masquerade", 3)
        #         date_check = False
        #
        #     while gift_check is True:
        #         gifting("watch", 2, gift["quantity-1"])
        #         gift_check = False
        #
        #     if GUTS is False:
        #         while GUTS is False:
        #             hobby_toggle("guts", "on")
        #             pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
        #                                                      region=coordinates["ui-guys"],
        #                                                      grayscale=True))
        #
        #     pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
        #                                              region=coordinates["guys-talk"],
        #                                              grayscale=True))
        # advance_relationship()
        # guy_toggle("kelby", "demihuman")
        # time.sleep(0.5)
        #
        # # Kelby Crush to Sweetheart
        # date_check = True
        # gift_check = True
        # while not pyautogui.locateOnScreen(requirements["requirement_kelby_crush"],
        #                                    region=coordinates["requirements"],
        #                                    grayscale=True):
        #
        #     while date_check is True:
        #         dating("boat-ride", 6)
        #         date_check = False
        #
        #     while gift_check is True:
        #         time.sleep(1)
        #         gifting("tools", 2, gift["quantity-1"])
        #         gift_check = False
        #
        #     if GAMER is False:
        #         while GAMER is False:
        #             hobby_toggle("gamer", "on")
        #             pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
        #                                                      region=coordinates["ui-guys"],
        #                                                      grayscale=True))
        #
        #     pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
        #                                              region=coordinates["guys-talk"],
        #                                              grayscale=True))
        # advance_relationship()
        #
        # # Kelby Sweetheart to Boyfriend
        # date_check = True
        # gift_check = True
        # while not pyautogui.locateOnScreen(requirements["requirement_kelby_sweetheart"],
        #                                    region=coordinates["requirements"],
        #                                    grayscale=True):
        #
        #     while date_check is True:
        #         dating("coaster", 6)
        #         date_check = False
        #
        #     while gift_check is True:
        #         gifting("watch", 2, gift["quantity-1"])
        #         gift_check = False
        #
        #     if SMART is False:
        #         while SMART is False:
        #             hobby_toggle("smart", "on")
        #             pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
        #                                                      region=coordinates["ui-guys"],
        #                                                      grayscale=True))
        #
        #     pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
        #                                              region=coordinates["guys-talk"],
        #                                              grayscale=True))
        # advance_relationship()
        #
        # # Kelby Boyfriend to Lover
        # date_check = True
        # gift_check = True
        # while not pyautogui.locateOnScreen(requirements["requirement_kelby_boyfriend"],
        #                                    region=coordinates["requirements"],
        #                                    grayscale=True):
        #
        #     while date_check is True:
        #         dating("carnival", 6)
        #         date_check = False
        #
        #     while gift_check is True:
        #         gifting("coffee", 1, gift["quantity-1m"])
        #         gift_check = False
        #
        #     if CARING is False:
        #         while CARING is False:
        #             hobby_toggle("caring", "on")
        #             pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
        #                                                      region=coordinates["ui-guys"],
        #                                                      grayscale=True))
        #
        #     pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
        #                                              region=coordinates["guys-talk"],
        #                                              grayscale=True))
        # advance_relationship()
        # guy_toggle("eli", "demihuman")
        # time.sleep(0.5)
        #
        # # The following lines of code take too long to begin >1 minute @ \
        # # Reset Boost: 1720, Per. Speed Boost: 8x, == $ 1 Billion to complete ==
        # # Eli Sweetheart to Boyfriend
        # date_check = True
        # gift_check = True
        # while not pyautogui.locateOnScreen(requirements["requirement_eli_sweetheart"],
        #                                    region=coordinates["requirements"],
        #                                    grayscale=True):
        #
        #     while date_check is True:
        #         dating("coaster", 10)
        #         date_check = False
        #
        #     while gift_check is True:
        #         gifting("ice-cream", 1, gift["quantity-100k"])
        #         gift_check = False
        #
        #     if CREATIVE is False:
        #         while CREATIVE is False:
        #             hobby_toggle("creative", "on")
        #             pyautogui.click(pyautogui.locateOnScreen(icon["ui-guys"],
        #                                                      region=coordinates["ui-guys"],
        #                                                      grayscale=True))
        #
        #     pyautogui.click(pyautogui.locateOnScreen(icon["guys-talk"],
        #                                              region=coordinates["guys-talk"],
        #                                              grayscale=True))
        # advance_relationship()

        reset = True
    soft_reset()

# pyautogui.click(pyautogui.locatedOnScreen)


