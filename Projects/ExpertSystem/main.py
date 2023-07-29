# Sample Knowledge Base for Vasireddy Venkatadri Institute of Technology (VVIT)

knowledge_base = {
    "General Information": {
        "Name": "Vasireddy Venkatadri Institute of Technology (VVIT)",
        "Established": "2007",
        "Founder": "Er. Vasireddy Vidya Sagar",
        "Location": "Nambur Village, Guntur, Andhra Pradesh, India",
        "Intake Capacity": "1620 B.Tech students and 72 M.Tech students annually",
        "Total Students": "More than 6000",
        "Teaching Staff": "345",
        "Non-Teaching Staff": "225",
        "Affiliation": "Jawaharlal Nehru Technological University, Kakinada (JNTUK)",
        "Accreditations": "NBA accredited B.Tech programs",
        "NAAC Grade": "A",
    },
    "Academic Programs": {
        "B.Tech Programs": ["CE", "EEE", "ME", "ECE", "CSE", "IT", "CSM", "CSO", "CIC", "AIM", "AID"],
        "M.Tech Programs": ["CSE", "VLSI&ES", "PEED", "MD", "SE"],
    },
    "Recognitions": {
        "MoUs with Industry and Training Companies": ["Infosys", "Tech Mahindra", "Social Agro", "Efftronics", "AMCAT", "Cocubes"],
        "Nodal Centre for Skill Development Programs of APSSDC, Govt. of AP": "2014",
        "Tie-ups with Premier Institutes": ["ISB", "Stanford University USA", "Northeastern University, Boston"],
        "Centre of Excellence (CoE) by Siemens India": "Established in 2016 under MoU with APSSDC",
        "Research Achievements": {
            "Completed DST Projects": 10,
            "Running DST Projects": 6,
            "Patents": 13,
            "Books Published": 16,
            "Journal Papers Published": 690,
        },
    },
    "Facilities": {
        "Libraries": {
            "Departmental Libraries": "Available",
            "Central Library": {
                "Student Book Bank": "Available for all students",
                "Access to e-journals": "Available",
                "NPTEL and IUCEE Access": "Available",
            },
        },
        "Infrastructure": {
            "Air-conditioned Classrooms": "Available",
            "Seminar Halls": "Available",
            "Multimodal Teaching Methodology": "Followed",
            "Indoor Sports Arena": "Available",
            "Outdoor Grounds with 400m Athletic Track": "Available",
        },
        "Hostels": {
            "Homely Hostels": "Available",
        },
        "Other Facilities": {
            "In-House Placement Training Team": "Available",
            "125 Mbps Dedicated Internet Connectivity": "Available",
            "100 KW Rooftop Grid Tied Solar Plant": "Available",
            "Fleet of 70 Buses for Transport": "Available",
            "Mineral Water Plant": "Available",
            "250KVA and 80KVA Generators": "Available",
        },
    },
    "Placements": {
        "Companies Recruiting Students": [
            "Tech Mahindra",
            "Infosys",
            "TCS",
            "Wipro",
            "Athena Health Care",
            "Open Text",
            "Genpact",
            "Sutherlands",
            "CSS Corp",
            "Convergys",
            "Apps Associates",
            # Add more companies as required...
        ],
        "Number of Companies": "Approximately 50 companies every year",
    },
    "Student Activities": {
        "Student Activity Council (SAC)": "Active student body on the campus",
        "Clubs and Competitions": "Annual Intercollegiate and Inter-University Cultural and Sporting Competitions (VIVA-VVIT)",
        "Volunteering Opportunities": ["NCC", "NSS", "SAC Forum"],
    },
    "Contact Information": {
        "Address": "Vasireddy Venkatadri Institute of Technology, Nambur (V), Peda Kakani (Md), Guntur (Dt), Andhra Pradesh, 522508",
        "Phone": "Add phone number here",
    },
}


def search_knowledge_base(query):
    result = []
    for category, data in knowledge_base.items():
        if isinstance(data, dict):
            for key, value in data.items():
                if query.lower() in key.lower():
                    result.append((category, key, value))
                elif isinstance(value, list) and any(query.lower() in item.lower() for item in value):
                    result.append((category, key, value))
        else:
            if query.lower() in data.lower():
                result.append((category, data))

    return result

if __name__ == '__main__':
    # Sample queries
    query1 = "Number of B.Tech programs"
    query2 = "Companies for placements"
    query3 = "Location of VVIT"

    # Search the knowledge base for the queries
    result1 = search_knowledge_base(query1)
    result2 = search_knowledge_base(query2)
    result3 = search_knowledge_base(query3)

    # Display the results
    print(f"Query: {query1}")
    for r in result1:
        print(f"{r[0]} -> {r[1]}: {r[2]}")

    print(f"\nQuery: {query2}")
    for r in result2:
        print(f"{r[0]} -> {r[1]}: {r[2]}")

    print(f"\nQuery: {query3}")
    for r in result3:
        print(f"{r[0]} -> {r[1]}: {r[2]}")