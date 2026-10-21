import json, sys
out = sys.argv[1]
L = "smart-laser-cat-toy-camera"
F = "smart-automatic-pet-feeder"
faq_blocks = {
 "q1": ("How long does shipping take?", "<p>Orders are processed within 1–3 business days. Delivery to the US, Canada and Mexico typically takes 7–15 business days. Shipping is always free and every order includes a tracking number.</p>"),
 "q2": ("How does the 20% bundle discount work?", "<p>Add both the Smart Automatic Pet Feeder and the Smart Laser Cat Toy to your cart and 20% is taken off automatically at checkout — no code needed.</p>"),
 "q3": ("What if my pet doesn't like it?", "<p>You're covered by our 30-day money-back guarantee. Contact us within 30 days of delivery and we'll help you with a return and full refund.</p>"),
 "q4": ("Do I need Wi-Fi for the feeder?", "<p>Only for the Wi-Fi models, which you control from your phone. The Classic Button model works on its own with simple one-touch scheduling.</p>"),
 "q5": ("Is the laser safe for my cat?", "<p>Yes, when used as intended. Never point the laser directly at eyes, and finish each session with a toy your cat can catch to keep playtime satisfying.</p>"),
 "q6": ("Is checkout secure?", "<p>Absolutely. Payments are processed through Shopify's encrypted checkout. We never see or store your card details.</p>"),
}
def faq(keys, pt=64):
    return {"type": "mt-faq", "blocks": {k: {"type": "question", "settings": {"question": faq_blocks[k][0], "answer": faq_blocks[k][1]}} for k in keys},
            "block_order": keys, "settings": {"eyebrow": "Questions?", "heading": "Frequently asked questions", "open_first": True, "heading_size": 40, "padding_top": pt, "padding_bottom": 80}}
trust = {"type": "mt-trust-bar", "blocks": {
  "t1": {"type": "item", "settings": {"icon": "truck", "title": "Free tracked shipping", "text": "US, Canada & Mexico"}},
  "t2": {"type": "item", "settings": {"icon": "return", "title": "30-day guarantee", "text": "Love it or your money back"}},
  "t3": {"type": "item", "settings": {"icon": "lock", "title": "Secure checkout", "text": "Encrypted payments"}},
  "t4": {"type": "item", "settings": {"icon": "chat", "title": "Friendly support", "text": "Real people, fast replies"}}},
  "block_order": ["t1","t2","t3","t4"], "settings": {"title_size": 14, "padding_top": 8, "padding_bottom": 8}}
guarantee = {"type": "mt-guarantee", "settings": {"seal_number": "30", "seal_text": "Day guarantee", "heading": "Love it or your money back",
  "body": "Try it at home for 30 days. If your pet isn't loving it, just contact us and we'll make it right with a full refund. Every order ships free with tracking, so you always know where it is.", "heading_size": 32, "padding_top": 40, "padding_bottom": 40}}
bundle = lambda pt=40, pb=40: {"type": "mt-bundle", "settings": {"product_a": F, "product_b": L, "percentage": 20, "tag": "Bundle & save 20%", "heading": "The complete smart-care set",
  "body": "Meals on schedule and playtime on demand. Get the Smart Feeder and the Laser Cat Toy together and save 20% — applied automatically at checkout.",
  "save_label": "You save [pct]%", "button": "Add both to cart", "loading_text": "Adding…", "fine": "20% off applied automatically at checkout · Free tracked shipping · 30-day guarantee", "bg": "#e6f0ec", "heading_size": 40, "padding_top": pt, "padding_bottom": pb}}

index = {"sections": {
 "hero": {"type": "mt-hero", "settings": {"eyebrow": "Smart pet care", "headline": "Happier pets,\neven when you're away.",
   "body": "Feed them on time and keep them playing from anywhere. Two smart essentials designed for busy pet parents.",
   "btn1_text": "Shop the bundle — save 20%", "btn2_text": "Explore products",
   "note": "Free tracked shipping · 30-day money-back guarantee", "badge": "Get both & save 20%", "product_1": F, "product_2": L,
   "text_align": "left", "heading_size": 64, "body_size": 18, "padding_top": 56, "padding_bottom": 48}},
 "trust": trust,
 "products": {"type": "mt-products", "blocks": {
   "c1": {"type": "product", "settings": {"product": F, "tag": "Bestseller", "text": "Scheduled, perfectly portioned meals — from buttons or your phone."}},
   "c2": {"type": "product", "settings": {"product": L, "tag": "New", "text": "Check in and start laser playtime from anywhere."}}},
   "block_order": ["c1","c2"], "settings": {"eyebrow": "The essentials", "heading": "Two smart products. One happy pet.", "body": "", "link_text": "Shop now", "text_align": "center", "heading_size": 44, "padding_top": 80, "padding_bottom": 40}},
 "bundle": bundle(),
 "feat_feeder": {"type": "mt-feature", "settings": {"product": F, "product_image_number": 1, "reverse": False, "eyebrow": "Smart Automatic Pet Feeder", "heading": "Meals on time, every time",
   "body": "Running late? Long day at work? Your pet still eats on schedule, with the right portion every time.",
   "points": "Large 4L capacity — fewer refills\nSchedule meals by button or from your phone\nOptional HD camera to watch mealtime live\nDetachable parts for quick, easy cleaning", "btn_text": "Shop the feeder", "heading_size": 40, "body_size": 17, "padding_top": 72, "padding_bottom": 40}},
 "feat_laser": {"type": "mt-feature", "settings": {"product": L, "product_image_number": 1, "reverse": True, "eyebrow": "Smart Laser Cat Toy & Pet Camera", "heading": "Playtime, wherever you are",
   "body": "Indoor cats need to hunt, chase and pounce. Start a laser game from your phone and see them having fun.",
   "points": "Remote laser play from your phone\nBuilt-in camera to check in anytime\nBurns energy and reduces boredom\nCompact, clean design for any room", "btn_text": "Shop the laser toy", "heading_size": 40, "body_size": 17, "padding_top": 40, "padding_bottom": 56}},
 "guarantee": guarantee,
 "faq": faq(["q1","q2","q3","q4","q5","q6"])},
 "order": ["hero","trust","products","bundle","feat_feeder","feat_laser","guarantee","faq"]}

def pdp(subtitle, accs, feats):
    blocks = {
      "p1": {"type": "perk", "settings": {"icon": "truck", "text": "Free tracked shipping to US, CA & MX"}},
      "p2": {"type": "perk", "settings": {"icon": "return", "text": "30-day money-back guarantee"}},
      "p3": {"type": "perk", "settings": {"icon": "shield", "text": "Secure, encrypted checkout"}},
      "p4": {"type": "perk", "settings": {"icon": "chat", "text": "Friendly support, fast replies"}},
      "a1": {"type": "accordion", "settings": {"title": "Description", "use_description": True, "content": "", "open": True}},
      "a2": {"type": "accordion", "settings": {"title": "Shipping & tracking", "use_description": False, "content": "<p>Free tracked shipping to the United States, Canada and Mexico. Orders are processed within 1–3 business days and typically arrive in 7–15 business days. You'll receive a tracking number by email as soon as your order ships.</p>", "open": False}},
      "a3": {"type": "accordion", "settings": {"title": "30-day money-back guarantee", "use_description": False, "content": "<p>Not happy? Contact us within 30 days of delivery and we'll arrange a return and full refund. No complicated forms.</p>", "open": False}},
    }
    order = ["p1","p2","p3","p4","a1","a2","a3"]
    for k,(t,c) in accs.items():
        blocks[k] = {"type": "accordion", "settings": {"title": t, "use_description": False, "content": c, "open": False}}
        order.insert(5, k)
    main = {"type": "mt-product", "blocks": blocks, "block_order": order, "settings": {
      "badge": "Bestseller", "subtitle": subtitle, "price_note": "Free tracked shipping included · Taxes calculated at checkout", "title_size": 40, "max_thumbs": 12,
      "show_stock": True, "low_stock": 15, "low_stock_text": "Hurry — only [count] left in stock", "in_stock_text": "In stock — ready to ship",
      "show_countdown": True, "cutoff_hour": 16, "countdown_text": "Order within [time] to get it processed today", "weekend_text": "Order now — processed first thing Monday",
      "urgency_text": "Holiday season is our busiest time — order early to get it on time",
      "atc_text": "Add to cart", "soldout_text": "Sold out", "unavailable_text": "Unavailable", "show_dynamic": True, "pill_limit": 4, "show_sticky": True,
      "show_bundle": True, "bundle_product_a": F, "bundle_product_b": L, "bundle_pct": 20, "bundle_title": "Complete the set & save 20%", "bundle_this_text": "This item",
      "bundle_total_text": "Bundle price", "bundle_button": "Add both & save 20%", "show_payment": True, "payment_text": "Secure, encrypted checkout", "padding_top": 32, "padding_bottom": 48}}
    secs = {"main": main, "trust": trust}
    ordr = ["main","trust"]
    for i,f in enumerate(feats):
        secs[f"feat{i}"] = {"type": "mt-feature", "settings": f}; ordr.append(f"feat{i}")
    secs["bundle"] = bundle(48, 24); secs["guarantee"] = guarantee; secs["faq"] = faq(["q1","q2","q3","q6"], 48)
    ordr += ["bundle","guarantee","faq"]
    return {"sections": secs, "order": ordr}

ft = lambda p, n, rev, eb, h, b, pts: {"product": p, "product_image_number": n, "reverse": rev, "eyebrow": eb, "heading": h, "body": b, "points": pts, "btn_text": "", "heading_size": 36, "body_size": 17, "padding_top": 48, "padding_bottom": 48}
laser = pdp("Check in on your cat and start laser playtime from your phone — so they stay active and happy while you're away.",
  {"a4": ("What's in the box", "<ul><li>1 × Smart Laser Cat Toy & Pet Camera</li><li>User manual</li></ul>")},
  [ft(L, 2, False, "Why cats love it", "A hunting game they never get bored of", "Unpredictable laser patterns trigger your cat's natural instinct to chase and pounce.", "Keeps indoor cats active\nHelps prevent boredom and weight gain\nStart a session from anywhere"),
   ft(L, 3, True, "Peace of mind", "See what they're up to", "Use the built-in camera to check in on your pet during the day.", "Check in from your phone\nCompact white design\nLightweight — about 1.1 lb")])
feeder = pdp("Perfectly portioned meals on a schedule you set — by button or from your phone. Your pet eats on time, even on busy days.",
  {"a4": ("Which model is right for me?", "<ul><li><strong>Classic Button 4L</strong> — simple one-touch scheduling, no Wi-Fi needed.</li><li><strong>Wi-Fi App 4L</strong> — schedule and adjust meals from your phone.</li><li><strong>Wi-Fi + HD Camera</strong> — watch mealtime live and talk to your pet.</li><li><strong>+ Water Fountain sets</strong> — add a USB running-water fountain for a complete feeding station.</li></ul>")},
  [ft(F, 2, False, "Built for busy days", "Never miss a meal again", "Set it once and relax — meals are served on time with the right portion.", "Large 4L capacity — fewer refills\nApp or one-touch button scheduling\nPlug-in power for reliable feeding"),
   ft(F, 3, True, "Easy to live with", "Simple to clean, safe to use", "Detachable parts and an optional 304 stainless steel bowl keep mealtime hygienic.", "Detachable, easy-clean design\nFood-safe materials\nIdeal for cats and small dogs")])
for name, data in [("index.json", index), ("product.mt-laser.json", laser), ("product.mt-feeder.json", feeder)]:
    with open(f"{out}/{name}", "w") as fh: json.dump(data, fh, indent=2, ensure_ascii=False)
print("ok")
