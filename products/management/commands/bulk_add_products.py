from decimal import Decimal
from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    help = 'Bulk add 102 products, mapped into existing categories only'

    # Maps each product-list category to your REAL existing category name
    CATEGORY_MAP = {
        "Cars": "Electronics",
        "Bikes": "Electronics",
        "Watches": "Accessories",
        "Headset": "Accessories",
        "Shoes": "Accessories",
        "Dresses": "Fashion",
        "Accessories": "Accessories",
        "Groceries": "Groceries",
        "Bags": "Luggage",
        "Food": "Home Food",
        "Laptops": "Electronics",
        "Mobiles": "Mobiles",
        "Fashion": "Fashion",
    }

    def handle(self, *args, **kwargs):
        products = [
            # --- CARS (8) -> Electronics ---
            ("Apex Velocity GT 2023", "apex-velocity-gt-2023", "6299999", "A premium sports sedan featuring a twin-turbo V8 engine, AI-assisted driving, adaptive suspension, panoramic glass roof, Matrix LED headlights, 360° camera system.", "Cars"),
            ("Soul Infinity SUV 2024", "soul-infinity-suv-2024", "7899999", "A luxury AI-powered SUV with Level-3 autonomous driving, hybrid powertrain, adaptive air suspension, panoramic OLED roof.", "Cars"),
            ("GodLike Hyper X 2025", "godlike-hyper-x-2025", "24999999", "A futuristic hypercar engineered with active aerodynamics, carbon fiber chassis, AI racing assistant, adaptive suspension.", "Cars"),
            ("OR Quantum EV 2026", "or-quantum-ev-2026", "12999999", "A next-generation electric luxury sedan with solid-state batteries, AI autonomous driving, augmented reality windshield.", "Cars"),
            ("DK Titan X SUV 2027", "dk-titan-x-suv-2027", "15899999", "A premium hyper SUV combining luxury and off-road capability with AI terrain adaptation, active suspension.", "Cars"),
            ("RNTX Phantom EV 2028", "rntx-phantom-ev-2028", "21999999", "An all-electric hypercar featuring quad electric motors, adaptive aerodynamic body, AI performance tuning.", "Cars"),
            ("AKOP Phantom GT 2029", "akop-phantom-gt-2029", "23999999", "A luxury grand touring coupe with butterfly doors, AI co-pilot, AR windshield, self-healing nano paint.", "Cars"),
            ("Raccer Formula X Concept", "raccer-formula-x-concept", "34999999", "The ultimate futuristic concept hypercar inspired by Formula racing, featuring an AI cockpit, magnetic suspension.", "Cars"),

            # --- BIKES (8) -> Electronics ---
            ("Apex RR2 Hyper Naked", "apex-rr2-hyper-naked", "1999999", "A premium streetfighter motorcycle featuring a 999cc DOHC engine, AI ride modes, ride-by-wire throttle, launch control.", "Bikes"),
            ("Soul NR1 Electric Superbike", "soul-nr1-electric-superbike", "2499999", "A futuristic electric superbike featuring solid-state batteries, AI riding assistant, instant torque, regenerative braking.", "Bikes"),
            ("GodLike GXR 1000", "godlike-gxr-1000", "2849999", "An AI-powered flagship superbike featuring active aerodynamic wings, carbon fiber body, electronic suspension.", "Bikes"),
            ("OR OR1000 Hyper Superbike", "or-or1000-hyper-superbike", "3099999", "Combines futuristic engineering with high performance, featuring AI riding assistance, adaptive aerodynamic winglets.", "Bikes"),
            ("DK 1200 RR", "dk-1200-rr", "3349999", "A next-generation superbike powered by a 1198cc engine producing 220 HP. Includes AI race mode, slide control.", "Bikes"),
            ("RNTX Storm RX", "rntx-storm-rx", "3699999", "An electric hyperbike with quad AI controllers, solid-state battery technology, adaptive winglets.", "Bikes"),
            ("AKOP Phantom R", "akop-phantom-r", "3999999", "A luxury performance superbike with adaptive cruise control, AI navigation, panoramic TFT cockpit.", "Bikes"),
            ("M416 Phantom Racer", "m416-phantom-racer", "4399999", "A concept superbike engineered for maximum performance with magnetic suspension, AI performance optimization.", "Bikes"),
            ("Raccer X1 Hyper Concept", "raccer-x1-hyper-concept", "4999999", "The ultimate futuristic superbike featuring quantum battery technology, AI autonomous ride modes, magnetic suspension.", "Bikes"),

            # --- WATCHES (6) -> Accessories ---
            ("CLICK Holograph Concept Timepiece", "click-holograph-concept-timepiece", "75000", "A futuristic concept watch with no traditional hands. Features a high-definition transparent micro-LED display.", "Watches"),
            ("TM Emerald Skeleton Automatic Watch", "tm-emerald-skeleton-automatic-watch", "450000", "A luxury analog watch featuring a complex open-heart automatic movement. Intricate gears visible through dial.", "Watches"),
            ("STOP Titanium Zero-Dial Watch", "stop-titanium-zero-dial-watch", "35000", "A minimalist, high-end watch. The circular casing is sandblasted matte titanium.", "Watches"),
            ("FIRE Forged Carbon Chronograph", "fire-forged-carbon-chronograph", "120000", "A rugged, oversized sports watch built for extreme conditions. The casing is forged carbon composite.", "Watches"),
            ("ION Titanium Mesh Hybrid Watch", "ion-titanium-mesh-hybrid-watch", "55000", "A sophisticated, ultra-slim hybrid smartwatch with a precision-machined titanium case.", "Watches"),
            ("Bg Deconstructed Architecture Timepiece", "bg-deconstructed-architecture-timepiece", "980000", "A complex, avant-garde wristwatch with a unique deconstructed design.", "Watches"),

            # --- HEADSET (6) -> Accessories ---
            ("WALKMORE Stride Active Headphones", "walkmore-stride-active-headphones", "14999", "A durable, wireless over-ear headset designed for active urban use with plush memory foam earcups.", "Headset"),
            ("FASTER Velocity Carbon Headset", "faster-velocity-carbon-headset", "24900", "A premium, lightweight wireless headset optimized for speed and performance with carbon fiber texture.", "Headset"),
            ("CLIMB Summit Audiophile Headphones", "climb-summit-audiophile-headphones", "69995", "An ultra-premium, open-back audiophile headset with exotic materials like forged carbon fiber.", "Headset"),
            ("STRAP Anchor Rugged Utility Headset", "strap-anchor-rugged-utility-headset", "17950", "An industrial-strength, durable headset built for tough environments with military-green frame.", "Headset"),
            ("QUANTUM Nebula Smart Audio Device", "quantum-nebula-smart-audio-device", "45000", "A futuristic, seamless audio device with earcups sculpted from polished ceramic.", "Headset"),
            ("SIMPLE Open-Air Aluminum Headphones", "simple-open-air-aluminum-headphones", "12000", "A minimalist, high-key audiophile headset featuring an open-back design with aluminum mesh.", "Headset"),

            # --- SHOES (7) -> Accessories ---
            ("Quantum Neon Running Shoes", "quantum-neon-running-shoes", "3999", "Lightweight performance running shoes featuring a breathable black mesh upper with electric blue accents.", "Shoes"),
            ("FastRide Velocity Runner", "fastride-velocity-runner", "3499", "Stylish navy blue sports shoes with vibrant orange highlights, engineered with breathable knit fabric.", "Shoes"),
            ("Climax Hyper Sprint", "climax-hyper-sprint", "4299", "Premium black athletic sneakers featuring neon green and cyan detailing, futuristic midsole technology.", "Shoes"),
            ("StrideX Air Motion", "stridex-air-motion", "3799", "Modern white running shoes with bold orange accents, breathable engineered mesh, ergonomic cushioning.", "Shoes"),
            ("Quantum Aero Pro", "quantum-aero-pro", "4199", "Performance-focused teal and black sports shoes with advanced air-cushion technology.", "Shoes"),
            ("Elevate Neo Runner", "elevate-neo-runner", "4599", "High-performance black and neon-green running shoes with ultra-lightweight construction.", "Shoes"),
            ("Strap Fusion X", "strap-fusion-x", "3899", "Premium navy and aqua athletic shoes featuring a breathable mesh upper, shock-absorbing EVA sole.", "Shoes"),
            ("GLM Aero Flex", "glm-aero-flex", "4099", "Contemporary grey and navy sports shoes with lime green accents, lightweight knitted upper.", "Shoes"),

            # --- DRESSES (7) -> Fashion ---
            ("Classic Elegance Combo", "classic-elegance-combo", "19999", "A refined monochrome combo featuring a black full-sleeve shirt layered over a white crew neck tee.", "Dresses"),
            ("Veloris Modern Essentials Combo", "veloris-modern-essentials-combo", "21999", "An earthy, elevated combo built around an olive green overshirt layered over a white tee.", "Dresses"),
            ("Acronym Tactical Combo", "acronym-tactical-combo", "52999", "A rugged, technical combo featuring a black Acronym utility jacket and grey cargo pants.", "Dresses"),
            ("Tailored Wool Blazer Combo", "tailored-wool-blazer-combo", "27999", "A sophisticated tailored combo featuring a grey wool blazer and matching trousers.", "Dresses"),
            ("Deconstructed Blazer Street Combo", "deconstructed-blazer-street-combo", "25999", "An edgy, layered combo pairing a distressed grey wool blazer with an ivory lace-trim camisole.", "Dresses"),
            ("Puff Sleeve Peplum Combo", "puff-sleeve-peplum-combo", "12999", "An elegant everyday combo featuring a white puff sleeve peplum top paired with flowing olive green trousers.", "Dresses"),
            ("Coastal Summer Dress Combo", "coastal-summer-dress-combo", "10999", "A breezy summer combo centered on a white floral embroidered sundress.", "Dresses"),

            # --- ACCESSORIES (8) -> Accessories ---
            ("Sapphire Hexagon Cufflinks", "sapphire-hexagon-cufflinks", "2499", "Sculptural hexagon-shaped cufflinks in brushed gunmetal with a blue sapphire-tone stone.", "Accessories"),
            ("Black Blue-Line Ring", "black-blue-line-ring", "1799", "A bold black matte-finish ring with a squared silhouette and glowing blue accent lines.", "Accessories"),
            ("Geometric Aviator Sunglasses", "geometric-aviator-sunglasses", "3299", "Angular, octagon-inspired aviator sunglasses in a gunmetal frame with gradient grey lenses.", "Accessories"),
            ("Woven Leather Panel Bracelet", "woven-leather-panel-bracelet", "1499", "A rugged bronze-tone bracelet combining woven leather panels with metal link detailing.", "Accessories"),
            ("Crystal Quartz Statement Necklace", "crystal-quartz-statement-necklace", "4999", "An artistic gold-wire necklace intricately wrapped with raw crystal quartz stones.", "Accessories"),
            ("Sapphire Angel Wing Brooch", "sapphire-angel-wing-brooch", "2999", "An elegant silver filigree brooch shaped like an angel wing with a blue sapphire-tone stone.", "Accessories"),
            ("Opal Drop Earrings with Diamond Bar", "opal-drop-earrings-diamond-bar", "8999", "Sophisticated dangle earrings featuring geometric diamond-studded bars suspending oval black opal drops.", "Accessories"),
            ("Coral Branch Gold Brooch", "coral-branch-gold-brooch", "2199", "An artisanal brooch shaped like a coral branch, finished in white enamel with gold accents.", "Accessories"),

            # --- GROCERIES (8) -> Groceries ---
            ("Basmati Rice", "basmati-rice", "199", "Premium long-grain basmati rice known for its fragrant aroma and fluffy texture when cooked.", "Groceries"),
            ("White Sugar", "white-sugar", "55", "Fine, pure white granulated sugar sourced for consistent sweetness.", "Groceries"),
            ("Iodized Salt", "iodized-salt", "25", "Refined iodized salt that adds essential flavor to everyday cooking.", "Groceries"),
            ("Mustard Oil", "mustard-oil", "179", "Cold-pressed mustard oil with a rich, pungent aroma and deep flavor.", "Groceries"),
            ("Atta Flour", "atta-flour", "249", "Stone-ground whole wheat atta flour, rich in fiber and nutrients.", "Groceries"),
            ("Red Lentils (Masoor Dal)", "red-lentils-masoor-dal", "129", "Premium quality split red lentils that cook quickly into a smooth, hearty dal.", "Groceries"),
            ("Black Tea Leaves", "black-tea-leaves", "149", "Robust, full-bodied black tea leaves with a rich aroma and deep color.", "Groceries"),
            ("Whole Red Chilies", "whole-red-chilies", "99", "Sun-dried whole red chilies with an intense heat and vibrant color.", "Groceries"),

            # --- BAGS (8) -> Luggage ---
            ("Lumina Circuit Tote Bag", "lumina-circuit-tote-bag", "3499", "A sleek black tote bag featuring a futuristic geometric print with circuit-board detailing.", "Bags"),
            ("Bronze Patchwork Chain Handbag", "bronze-patchwork-chain-handbag", "5999", "An artisanal bronze leather handbag with geometric patchwork panels and oversized chain handles.", "Bags"),
            ("Kera Scalloped Hobo Bag", "kera-scalloped-hobo-bag", "4299", "A textured off-white leather hobo bag with layered scalloped detailing.", "Bags"),
            ("Bearswift Tactical Backpack", "bearswift-tactical-backpack", "4999", "A rugged camouflage backpack with multiple orange-trimmed utility pockets.", "Bags"),
            ("Orbital Solar Explorer Backpack", "orbital-solar-explorer-backpack", "6499", "A durable iridescent backpack designed for outdoor exploration.", "Bags"),
            ("Neo-Caliber Urban Commuter Backpack", "neo-caliber-urban-commuter-backpack", "5499", "A sleek matte black backpack with an angular, armor-like design.", "Bags"),
            ("Hyperion Checked Suitcase", "hyperion-checked-suitcase", "8999", "A durable navy hardshell checked suitcase with a ribbed exterior and spinner wheels.", "Bags"),
            ("Tan Woven Leaf Hobo Bag", "tan-woven-leaf-hobo-bag", "3999", "A handcrafted tan leather hobo bag with woven strap detailing.", "Bags"),

            # --- FOOD (8) -> Home Food ---
            ("Tsukemono", "tsukemono", "199", "A traditional Japanese assortment of pickled vegetables.", "Food"),
            ("Tamago", "tamago", "249", "Soft, lightly sweetened Japanese rolled omelette.", "Food"),
            ("Wasabi & Ginger", "wasabi-and-ginger", "99", "A classic accompaniment duo featuring fresh grated wasabi paste and pickled sushi ginger.", "Food"),
            ("Steamed Jasmine Rice", "steamed-jasmine-rice", "149", "Fluffy, fragrant steamed jasmine rice, lightly garnished.", "Food"),
            ("Pork Gyoza", "pork-gyoza", "349", "Pan-seared Japanese dumplings filled with seasoned minced pork.", "Food"),
            ("Kimchi", "kimchi", "199", "Traditional Korean fermented napa cabbage in a spicy, tangy chili seasoning.", "Food"),
            ("Seaweed Salad", "seaweed-salad", "279", "Chilled marinated seaweed tossed in a sesame dressing.", "Food"),
            ("Edamame", "edamame", "179", "Steamed young soybeans lightly salted and served in the pod.", "Food"),

            # --- LAPTOPS (6) -> Electronics ---
            ("openAir 1.0", "openair-1-0", "139999", "The openAir 1.0 is an ultra-premium flagship laptop featuring an 18-inch 4K OLED bezel-less display, Intel Core i7 processor, AI Copilot key, transparent touchpad, fingerprint security, per-key RGB keyboard, wireless charging pad, Dolby Atmos audio, vapor chamber cooling, and an ultra-thin aluminum body.", "Laptops"),
            ("ProLab 1.0", "prolab-1-0", "149999", "ProLab 1.0 combines premium performance with modern engineering. It features an Intel Core i7 processor, 18-inch 4K OLED display, Dolby Atmos speakers, AI Copilot integration, transparent touchpad, RGB keyboard, vapor chamber cooling, and a premium white-blue aluminum finish.", "Laptops"),
            ("FireWork X1", "firework-x1", "169999", "FireWork X1 is a high-performance creator laptop with a bold futuristic design. It offers Intel Core i7 processing, AI optimization, 18-inch 4K OLED display, RGB keyboard, Dolby Atmos surround sound, advanced cooling system, and aerospace-grade construction.", "Laptops"),
            ("B God X1", "b-god-x1", "189999", "B God X1 introduces next-generation computing with holographic touch controls, AI Copilot, adaptive gesture recognition, intelligent sensor suite, Dolby Atmos audio, RGB Aura lighting, wireless charging, and an elegant futuristic design in radiant blue and red accents.", "Laptops"),
            ("Capture 2027", "capture-2027", "249999", "Capture 2027 is an ultra-premium AI flagship laptop built for the future. It features a stunning 8K Micro-LED display, Intel Core i9 processor, RTX-class graphics, Neural AI Engine, QuantumChill cooling, holographic touch interface, SolarCore hybrid charging, and titanium alloy body.", "Laptops"),
            ("Gangstar X1 Pro Gaming", "gangstar-x1-pro-gaming", "229999", "Gangstar X1 Pro Gaming is an elite gaming laptop built for competitive gamers. It features a 21-inch 4K AMOLED 240Hz display, Intel Core i9 processor, RTX-class gaming GPU, liquid metal cooling, per-key RGB mechanical keyboard, AI Game Booster, and Dolby Atmos surround sound.", "Laptops"),

            # --- MOBILES (6) -> Mobiles ---
            ("Guess Fusion X", "guess-fusion-x", "129999", "Guess Fusion X combines the best premium Android and iPhone flagship technologies into one device. It features a 6.9-inch LTPO AMOLED display, 200MP AI camera system, under-display Face ID, ultrasonic fingerprint scanner, satellite connectivity, AI assistant, titanium frame, IP69 water resistance, Wi-Fi 7, Dolby Atmos stereo speakers, 100W fast charging, and advanced AI photography.", "Mobiles"),
            ("Switch Neo Ultra", "switch-neo-ultra", "149999", "Switch Neo Ultra is a futuristic flagship smartphone engineered with the finest innovations of 2025. It features a 6.95-inch 2K LTPO AMOLED display, AI Neural Processor, adaptive refresh rate up to 165Hz, advanced periscope camera, satellite SOS, MagSafe-compatible wireless charging, AI translation, intelligent battery management, premium metal blue body, and next-generation security architecture.", "Mobiles"),
            ("Air 1 Infinity", "air-1-infinity", "169999", "Air 1 Infinity is a premium flagship smartphone built to outperform the competition. It features a Snapdragon Elite processor, 6.9-inch AMOLED 180Hz display, advanced vapor chamber cooling with micro-fan technology, AI gaming engine, 200MP quad-camera system, titanium frame, Wi-Fi 7, UWB, satellite communication, AI Copilot, Dolby Atmos audio, and ultra-fast charging for gamers and professionals.", "Mobiles"),
            ("GLM 5.1 Drone Edition", "glm-5-1-drone-edition", "249999", "GLM 5.1 Drone Edition redefines smartphone innovation with a detachable AI-powered drone camera capable of autonomous aerial photography and cinematic video capture. It features a 7-inch LTPO AMOLED display, AI Neural Engine, military-grade cybersecurity, quantum encryption, satellite connectivity, 240W HyperCharge, graphene battery technology, advanced cooling system, titanium ceramic construction, and next-generation holographic user interface.", "Mobiles"),
            ("JCloud Imperial X", "jcloud-imperial-x", "219999", "JCloud Imperial X delivers a luxury smartphone experience inspired by the latest premium flagship technologies. It features a titanium-gold frame, 6.9-inch Super Retina XDR OLED display, AI photography engine, under-display Face ID, MagSafe wireless ecosystem, satellite communication, spatial audio, AI personal assistant, secure hardware encryption, premium ceramic protection, and seamless ecosystem integration.", "Mobiles"),
            ("Smart Gaming Beast X", "smart-gaming-beast-x", "239999", "Smart Gaming Beast X is the ultimate gaming smartphone designed for esports enthusiasts. It features a 7-inch 240Hz AMOLED display, flagship gaming processor, advanced vapor chamber cooling with active fan, pressure-sensitive gaming triggers, AI Game Boost engine, RGB gaming lighting, Dolby Atmos quad speakers, 240W HyperCharge, Wi-Fi 7, low-latency gaming mode, premium metallic light blue and pink finish, and immersive gaming software optimized for competitive play.", "Mobiles"),

            # --- T-SHIRTS (9) -> Fashion ---
            ("openAir Aero Tee", "openair-aero-tee", "2499", "A premium performance T-shirt featuring an aerodynamic futuristic design with breathable fabric, moisture-wicking technology, and minimalist graphics. Designed for tech enthusiasts and everyday comfort.", "Fashion"),
            ("ProLab Quantum Tee", "prolab-quantum-tee", "2699", "A modern tech-inspired T-shirt with geometric patterns, premium cotton blend, antibacterial fabric, UV protection, and a sleek contemporary design for professionals.", "Fashion"),
            ("FireWork Blaze Tee", "firework-blaze-tee", "2799", "A bold streetwear T-shirt featuring dynamic graphics, high-density printing, breathable fabric, and a modern athletic fit inspired by futuristic technology.", "Fashion"),
            ("B God Nova Tee", "b-god-nova-tee", "2999", "A luxury lifestyle T-shirt crafted from premium cotton with metallic accents, AI-inspired graphics, soft-touch fabric, and superior comfort.", "Fashion"),
            ("Capture Vision Tee", "capture-vision-tee", "3299", "A futuristic fashion T-shirt featuring advanced graphic artwork, premium stretch fabric, anti-wrinkle technology, and lightweight construction.", "Fashion"),
            ("Gangstar Gaming Jersey", "gangstar-gaming-jersey", "3499", "An esports-inspired gaming jersey featuring breathable mesh fabric, sweat management technology, vibrant graphics, and a professional gaming fit.", "Fashion"),
            ("Air 1 Velocity Tee", "air1-velocity-tee", "2899", "A futuristic aviation-inspired T-shirt with premium microfiber fabric, lightweight construction, reflective accents, and ultra-soft comfort.", "Fashion"),
            ("GLM 5.1 Tech Jersey", "glm-5-1-tech-jersey", "3699", "A premium technology-inspired jersey featuring metallic design elements, breathable performance fabric, cooling mesh panels, and ergonomic athletic fit.", "Fashion"),
            ("JCloud Elite Tee", "jcloud-elite-tee", "3299", "A luxury fashion T-shirt with elegant gold accents, premium cotton blend, soft-touch finish, and sophisticated minimalist styling.", "Fashion"),

            # --- FASHION COMBOS (6) -> Fashion ---
            ("Aurelian Classic Combo", "aurelian-classic-combo", "8999", "Includes a premium black formal shirt, white crew-neck T-shirt, beige chinos, leather loafers, luxury wristwatch, sunglasses, and signature fragrance. Perfect for business casual and evening occasions.", "Fashion"),
            ("Veloris Urban Combo", "veloris-urban-combo", "9499", "Features an olive premium shirt, white T-shirt, cream chinos, white sneakers, leather watch, sunglasses, and premium perfume for a modern casual look.", "Fashion"),
            ("Nexvora Executive Combo", "nexvora-executive-combo", "10499", "Includes a navy blue luxury shirt, charcoal trousers, black Oxford shoes, stainless steel watch, leather belt, sunglasses, and premium fragrance designed for executives.", "Fashion"),
            ("Zephyron Street Combo", "zephyron-street-combo", "8799", "A stylish streetwear collection featuring an oversized graphic T-shirt, cargo pants, designer sneakers, smartwatch, cap, chain, and sunglasses for a trendy urban look.", "Fashion"),
            ("Lumivox Luxe Combo", "lumivox-luxe-combo", "11499", "A luxury fashion combo with a premium blazer, black turtleneck, tailored trousers, Chelsea boots, automatic watch, premium wallet, and signature perfume.", "Fashion"),
            ("Kryon Active Combo", "kryon-active-combo", "9999", "A performance-inspired outfit including a premium polo T-shirt, joggers, running shoes, fitness smartwatch, sports sunglasses, and lightweight backpack for active lifestyles.", "Fashion"),
        ]

        created_count = 0
        skipped_count = 0
        category_cache = {}

        for name, slug, price, desc, list_cat in products:
            real_cat_name = self.CATEGORY_MAP[list_cat]

            if real_cat_name not in category_cache:
                try:
                    category_cache[real_cat_name] = Category.objects.get(name=real_cat_name)
                except Category.DoesNotExist:
                    self.stderr.write(self.style.ERROR(
                        f'STOPPED: Category "{real_cat_name}" does not exist. Fix in admin, then re-run.'
                    ))
                    return

            category = category_cache[real_cat_name]

            product, created = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'category': category,
                    'price': Decimal(price),
                    'description': desc,
                }
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created: {name} -> {real_cat_name}'))
            else:
                skipped_count += 1
                self.stdout.write(f'Already exists, skipped: {name}')

        self.stdout.write(self.style.SUCCESS(
            f'\nDONE! Created {created_count} products, skipped {skipped_count} duplicates.'
        ))