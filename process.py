import json
import os

data = [
    {
        "module": "01 General Anatomy",
        "category": "General",
        "questions": [
            {
                "question": "What is the difference between the median plane and a sagittal plane?",
                "answer": "\u2022 Median plane: A single plane that bisects the body into equal left/right halves.\n\u2022 Sagittal plane: Any vertical plane parallel to the median plane.\n\u2022 Movements: Flexion and extension occur in the sagittal plane."
            },
            {
                "question": "Why is the metaphysis the most common site for osteosarcoma and osteomyelitis?",
                "answer": "\u2022 Sluggish blood flow: Wide, tortuous capillaries trap bacteria (Osteomyelitis).\n\u2022 Vulnerable cells: Rapidly dividing osteoblasts in growing teens are prone to mutation (Osteosarcoma)."
            },
            {
                "question": "What bones ossify by intramembranous ossification and why does it matter?",
                "answer": "\u2022 Bones: Flat skull bones, mandible, and clavicle shaft.\n\u2022 Mechanism: Direct bone formation without a cartilage template.\n\u2022 Importance: Allows fontanelles for brain growth/birth and dictates specific healing patterns."
            },
            {
                "question": "Why does articular cartilage not heal well after injury?",
                "answer": "\u2022 Avascular: No blood vessels means no inflammatory or clotting response.\n\u2022 No Perichondrium: Lacks progenitor cells for repair.\n\u2022 Low Turnover: Chondrocytes divide very slowly."
            },
            {
                "question": "What is the difference between a ligament and a tendon?",
                "answer": "\u2022 Tendon: Connects muscle to bone. Parallel fibers maximize strength; heals better due to some blood supply.\n\u2022 Ligament: Connects bone to bone. Multi-directional fibers stabilize joints; heals poorly due to poor blood supply."
            },
            {
                "question": "What is rigor mortis and what is its biochemical basis?",
                "answer": "\u2022 Definition: Post-mortem muscle stiffening.\n\u2022 Basis: Lack of ATP prevents myosin from detaching from actin, locking cross-bridges.\n\u2022 Timeline: Starts 2-6 hrs, peaks at 12 hrs, resolves 24-48 hrs."
            },
            {
                "question": "Classify bursae and give two examples of clinically important bursae around the knee.",
                "answer": "\u2022 True Bursae: Present normally, lined with synovium.\n\u2022 Adventitious Bursae: Form due to abnormal friction.\n\u2022 Suprapatellar: Communicates with knee joint cavity.\n\u2022 Prepatellar: Does not communicate; kneeling causes 'housemaid's knee'."
            }
        ]
    },
    {
        "module": "02 Upper Limb",
        "category": "Bones & Joints",
        "questions": [
            {
                "question": "What are the peculiarities of the clavicle?",
                "answer": "\u2022 Only long bone lying horizontally.\n\u2022 First to ossify (5-6 wks) but last epiphysis to fuse (22-25 yrs).\n\u2022 Intramembranous ossification and lacks a medullary cavity."
            },
            {
                "question": "Describe the scaphoid bone and its clinical importance.",
                "answer": "\u2022 Position: Lateral proximal carpal bone.\n\u2022 Blood Supply: Enters distally, risking proximal pole avascular necrosis in fractures.\n\u2022 Clinical: Fracture presents as anatomical snuffbox tenderness."
            }
        ]
    },
    {
        "module": "02 Upper Limb",
        "category": "Brachial Plexus & Nerves",
        "questions": [
            {
                "question": "Describe the formation and branches of the brachial plexus.",
                "answer": "\u2022 Roots (C5-T1), Trunks (Superior, Middle, Inferior), Divisions, Cords (Lateral, Medial, Posterior).\n\u2022 Terminal branches: Musculocutaneous, Median, Ulnar, Radial, Axillary."
            },
            {
                "question": "A patient presents with wrist drop after using crutches. Which nerve is injured and at what level?",
                "answer": "\u2022 Nerve: Radial nerve.\n\u2022 Level: High axilla (crutch palsy).\n\u2022 Signs: Wrist/finger drop AND elbow extension weakness (triceps affected)."
            },
            {
                "question": "Explain the \"ulnar paradox\" with reference to nerve injury levels.",
                "answer": "\u2022 Low Lesion (Wrist): Severe clawing (FDP intact to pull joints).\n\u2022 High Lesion (Elbow): Milder clawing (FDP paralyzed, unable to pull).\n\u2022 Paradox: A higher/worse injury results in less visible deformity."
            },
            {
                "question": "What is carpal tunnel syndrome? Give its anatomy, causes, and clinical features.",
                "answer": "\u2022 Anatomy: 9 tendons + Median nerve beneath flexor retinaculum.\n\u2022 Causes: Pregnancy, RA, repetitive use, hypothyroidism.\n\u2022 Signs: Tingling in lateral 3.5 fingers (worse at night), Thenar wasting, positive Tinel's/Phalen's signs."
            }
        ]
    },
    {
        "module": "02 Upper Limb",
        "category": "Axilla, Rotator Cuff & Applied",
        "questions": [
            {
                "question": "Name the contents of the axilla.",
                "answer": "\u2022 Vessels: Axillary artery & vein.\n\u2022 Nerves: Brachial plexus cords, long thoracic & intercostobrachial nerves.\n\u2022 Lymph Nodes: 5 groups.\n\u2022 Fat: Adipose tissue."
            },
            {
                "question": "Enumerate the muscles of the rotator cuff and their actions.",
                "answer": "\u2022 Supraspinatus: Initiates abduction (0-15\u00b0).\n\u2022 Infraspinatus & Teres Minor: Lateral rotation.\n\u2022 Subscapularis: Medial rotation.\n\u2022 Function: Compresses and stabilizes the glenohumeral joint."
            }
        ]
    },
    {
        "module": "03 Lower Limb",
        "category": "Joints & Bones",
        "questions": [
            {
                "question": "What is the blood supply to the head of the femur? Which vessel is most important and why?",
                "answer": "\u2022 Key Vessel: Medial circumflex femoral artery (MCFA).\n\u2022 Importance: Supplies majority of blood in adults via retinacular vessels.\n\u2022 Risk: Neck fractures tear these vessels, causing avascular necrosis."
            },
            {
                "question": "What is the \"unhappy triad\" and why is the lateral meniscus spared?",
                "answer": "\u2022 Triad: ACL + MCL + Medial meniscus.\n\u2022 Why Lateral Spared: Lateral meniscus is NOT attached to LCL (separated by popliteus), allowing it to escape tearing forces."
            },
            {
                "question": "What is the screw-home mechanism of the knee?",
                "answer": "\u2022 Locking: Tibia automatically rotates laterally in the last 10-15\u00b0 of extension, locking the knee.\n\u2022 Unlocking: Popliteus muscle medially rotates the tibia to initiate flexion."
            }
        ]
    },
    {
        "module": "03 Lower Limb",
        "category": "Spaces & Contents",
        "questions": [
            {
                "question": "Name the contents of the femoral triangle from lateral to medial.",
                "answer": "\u2022 N-A-V-E-L:\n\u2022 Nerve (Femoral, outside sheath).\n\u2022 Artery (Femoral, inside sheath).\n\u2022 Vein (Femoral, inside sheath).\n\u2022 Empty Space (Canal with Cloquet's node)."
            },
            {
                "question": "Which is the deepest structure in the popliteal fossa and why is this clinically important?",
                "answer": "\u2022 Deepest: Popliteal artery.\n\u2022 Risk: Highly vulnerable to tearing in supracondylar fractures or posterior knee dislocations, causing ischemia."
            }
        ]
    },
    {
        "module": "03 Lower Limb",
        "category": "Nerves & Clinical",
        "questions": [
            {
                "question": "Describe foot drop \u2014 cause, mechanism, clinical features, and gait.",
                "answer": "\u2022 Cause: Common peroneal nerve injury at fibula neck.\n\u2022 Mechanism: Loss of dorsiflexors and everters.\n\u2022 Signs: Foot hangs in plantarflexion/inversion; high-stepping gait to avoid toe drag."
            },
            {
                "question": "Why is referred pain felt in the knee in hip joint disease?",
                "answer": "\u2022 Hilton's Law: Nerves to a joint also supply moving muscles and skin.\n\u2022 Mechanism: Obturator nerve supplies BOTH hip and medial knee, so hip pain is referred centrally to the knee."
            },
            {
                "question": "What is Trendelenburg's sign? What are its causes?",
                "answer": "\u2022 Sign: Pelvis drops on the normal side when standing on the affected leg.\n\u2022 Cause: Weak gluteus medius/minimus (superior gluteal nerve damage, hip OA)."
            }
        ]
    },
    {
        "module": "04 Thorax",
        "category": "Thoracic Wall & Pleura",
        "questions": [
            {
                "question": "What structures pass through the sternal angle? What is its vertebral level?",
                "answer": "\u2022 Level: T4/T5 disc.\n\u2022 Structures: Trachea bifurcates, aortic arch begins/ends, azygos vein joins SVC."
            },
            {
                "question": "Where is the safe site for thoracocentesis? Why over the upper border of the rib?",
                "answer": "\u2022 Site: 7th-8th ICS, posterior axillary line.\n\u2022 Why: Needle placed over the upper rib border avoids the neurovascular bundle lying in the inferior costal groove."
            }
        ]
    },
    {
        "module": "04 Thorax",
        "category": "Bronchopulmonary Segments & Lungs",
        "questions": [
            {
                "question": "Define a bronchopulmonary segment. Why is it surgically important?",
                "answer": "\u2022 Definition: Smallest functional lung unit with its own bronchus and artery.\n\u2022 Surgery: Intersegmental veins allow safe removal of diseased segments while sparing healthy lung."
            },
            {
                "question": "Why do inhaled foreign bodies lodge more commonly in the right lung? And in which segment?",
                "answer": "\u2022 Why: Right main bronchus is wider, shorter, and more vertical.\n\u2022 Where: Posterior basal segment (erect) or Superior segment (supine) of right lower lobe."
            },
            {
                "question": "What is an eparterial bronchus? Where is it found?",
                "answer": "\u2022 Definition: A bronchus arising ABOVE the pulmonary artery.\n\u2022 Location: Right upper lobe bronchus only."
            }
        ]
    },
    {
        "module": "04 Thorax",
        "category": "Heart, Coronary Arteries & Conducting System",
        "questions": [
            {
                "question": "Where exactly is the SA node? What is its blood supply?",
                "answer": "\u2022 Location: Upper right atrium, right of crista terminalis near SVC.\n\u2022 Supply: SA nodal artery (usually from Right Coronary Artery)."
            },
            {
                "question": "Why does inferior myocardial infarction (MI) cause heart block?",
                "answer": "\u2022 Mechanism: Inferior MI involves the Right Coronary Artery (RCA).\n\u2022 Impact: RCA supplies both the SA and AV nodes, so ischemia disrupts conduction."
            },
            {
                "question": "What is the Triangle of Koch? What structure lies at its apex?",
                "answer": "\u2022 Borders: Tricuspid valve, Tendon of Todaro, Coronary sinus orifice.\n\u2022 Apex: AV node.\n\u2022 Clinical: Targeted in ablation for tachycardias."
            },
            {
                "question": "What is the 'artery of sudden death' and why is it called so?",
                "answer": "\u2022 Artery: Left Anterior Descending (LAD) artery.\n\u2022 Why: Supplies massive anterior left ventricle territory; occlusion causes rapid shock and death."
            }
        ]
    },
    {
        "module": "04 Thorax",
        "category": "Pericardium, Mediastinum & Diaphragm",
        "questions": [
            {
                "question": "Name the structures passing through the diaphragm at T8, T10, and T12.",
                "answer": "\u2022 T8: IVC, Right phrenic nerve.\n\u2022 T10: Esophagus, Vagus nerves.\n\u2022 T12: Aorta, Thoracic duct, Azygos vein."
            },
            {
                "question": "What is the significance of the pericardial transverse sinus in cardiac surgery?",
                "answer": "\u2022 Location: Behind ascending aorta/pulmonary trunk.\n\u2022 Use: Surgeons pass a finger through to simultaneously clamp both outflow tracts to control bleeding."
            }
        ]
    }
]

output_path = r"c:\Users\sayan\Downloads\biochem Note X\anatomy_viva_questions.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("JSON file successfully created and verified.")
