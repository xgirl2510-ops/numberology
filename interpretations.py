"""
Numerology Interpretations - Luận giải các chỉ số Thần Số Học
Chứa ý nghĩa chi tiết cho từng số từ 1-9 và Master Numbers (11, 22, 33)
"""

# ========== LIFE PATH NUMBER (Chỉ Số Đường Đời) ==========
LIFE_PATH = {
    1: {
        "title": "Người Lãnh Đạo - The Leader",
        "keywords": ["Độc lập", "Tiên phong", "Sáng tạo", "Quyết đoán", "Tự tin"],
        "description": """
Bạn sinh ra để dẫn đầu và khởi xướng. Là người tiên phong, bạn có khả năng
độc lập và sáng tạo mạnh mẽ. Bạn không thích bị kiểm soát và luôn muốn làm
theo cách của mình. Tham vọng và quyết tâm là động lực chính của bạn.
""",
        "strengths": ["Lãnh đạo tự nhiên", "Tự tin cao", "Sáng tạo", "Tiên phong"],
        "challenges": ["Bướng bỉnh", "Ích kỷ", "Thiếu kiên nhẫn", "Cô đơn"],
        "career": ["Doanh nhân", "CEO", "Nhà phát minh", "Chính trị gia", "Nghệ sĩ độc lập"]
    },

    2: {
        "title": "Người Hòa Giải - The Peacemaker",
        "keywords": ["Hợp tác", "Nhạy cảm", "Ngoại giao", "Hòa bình", "Đối tác"],
        "description": """
Bạn là người hòa giải tự nhiên, có khả năng nhìn nhận nhiều góc độ và mang
mọi người lại với nhau. Bạn nhạy cảm, chu đáo và thích làm việc theo nhóm.
Mối quan hệ và sự hài hòa rất quan trọng với bạn.
""",
        "strengths": ["Ngoại giao", "Nhạy cảm", "Hợp tác tốt", "Kiên nhẫn"],
        "challenges": ["Thiếu tự tin", "Quá nhạy cảm", "Do dự", "Tránh đối đầu"],
        "career": ["Trung gian hòa giải", "Tư vấn", "Ngoại giao", "Dịch vụ khách hàng", "Nghệ thuật"]
    },

    3: {
        "title": "Người Sáng Tạo - The Creative",
        "keywords": ["Sáng tạo", "Giao tiếp", "Vui vẻ", "Biểu đạt", "Nghệ thuật"],
        "description": """
Bạn là người sáng tạo, vui vẻ và có khiếu giao tiếp tuyệt vời. Bạn thích
thể hiện bản thân qua nghệ thuật, lời nói hoặc văn bản. Tính lạc quan và
khả năng truyền cảm hứng là điểm mạnh của bạn.
""",
        "strengths": ["Sáng tạo", "Giao tiếp tốt", "Lạc quan", "Nghệ thuật"],
        "challenges": ["Thiếu tập trung", "Hoang phí năng lượng", "Nông cạn", "Thiếu kỷ luật"],
        "career": ["Nghệ sĩ", "Nhà văn", "Diễn giả", "Giải trí", "Marketing"]
    },

    4: {
        "title": "Người Xây Dựng - The Builder",
        "keywords": ["Thực tế", "Kỷ luật", "Tổ chức", "Chăm chỉ", "Ổn định"],
        "description": """
Bạn là người thực tế, có tổ chức và đáng tin cậy. Bạn thích xây dựng nền
tảng vững chắc và làm việc chăm chỉ để đạt mục tiêu. Kỷ luật và trách
nhiệm là giá trị cốt lõi của bạn.
""",
        "strengths": ["Có tổ chức", "Đáng tin cậy", "Thực tế", "Kiên trì"],
        "challenges": ["Cứng nhắc", "Thiếu linh hoạt", "Quá nghiêm túc", "Sợ thay đổi"],
        "career": ["Kế toán", "Kỹ sư", "Kiến trúc sư", "Quản lý dự án", "Ngân hàng"]
    },

    5: {
        "title": "Người Tự Do - The Freedom Seeker",
        "keywords": ["Tự do", "Phiêu lưu", "Thay đổi", "Linh hoạt", "Đa năng"],
        "description": """
Bạn khao khát tự do và trải nghiệm mới. Bạn thích phiêu lưu, du lịch và
thay đổi. Sự đa năng và khả năng thích nghi là điểm mạnh của bạn. Bạn không
thích bị ràng buộc.
""",
        "strengths": ["Linh hoạt", "Phiêu lưu", "Đa năng", "Thích nghi tốt"],
        "challenges": ["Thiếu cam kết", "Bồn chồn", "Thiếu kiên nhẫn", "Vội vàng"],
        "career": ["Du lịch", "Báo chí", "Bán hàng", "Marketing", "Diễn giả"]
    },

    6: {
        "title": "Người Nuôi Dưỡng - The Nurturer",
        "keywords": ["Trách nhiệm", "Chăm sóc", "Gia đình", "Hòa hợp", "Phục vụ"],
        "description": """
Bạn có trách nhiệm cao và thích chăm sóc người khác. Gia đình và cộng đồng
rất quan trọng với bạn. Bạn tìm kiếm sự hài hòa và cân bằng trong mọi mối
quan hệ.
""",
        "strengths": ["Có trách nhiệm", "Chăm sóc tốt", "Hài hòa", "Đáng tin cậy"],
        "challenges": ["Kiểm soát quá mức", "Tự hy sinh", "Lo lắng", "Hoàn hảo chủ nghĩa"],
        "career": ["Giáo viên", "Y tế", "Tư vấn", "Thiết kế nội thất", "Nghệ thuật"]
    },

    7: {
        "title": "Người Tìm Kiếm Chân Lý - The Seeker",
        "keywords": ["Phân tích", "Tâm linh", "Trí tuệ", "Nội tâm", "Hoàn hảo"],
        "description": """
Bạn là người trí tuệ, sâu sắc và thích tìm kiếm chân lý. Bạn cần thời gian
một mình để suy ngẫm và phân tích. Tâm linh và kiến thức là ưu tiên của bạn.
""",
        "strengths": ["Trí tuệ", "Phân tích sâu", "Trực giác", "Hoàn hảo"],
        "challenges": ["Cô lập", "Bi quan", "Nghi ngờ", "Khó gần"],
        "career": ["Nhà khoa học", "Nghiên cứu", "Tâm linh", "Triết học", "Công nghệ"]
    },

    8: {
        "title": "Người Thành Đạt - The Powerhouse",
        "keywords": ["Thành công", "Quyền lực", "Vật chất", "Tham vọng", "Tổ chức"],
        "description": """
Bạn có tham vọng lớn và khả năng đạt được thành công vật chất. Bạn hiểu về
tiền bạc, quyền lực và cách tổ chức. Bạn sinh ra để đạt được những thành
tựu lớn lao.
""",
        "strengths": ["Tổ chức tốt", "Tham vọng", "Hiệu quả", "Quyền lực"],
        "challenges": ["Vật chất hóa", "Độc đoán", "Căng thẳng", "Bỏ bê tâm linh"],
        "career": ["CEO", "Doanh nhân", "Ngân hàng", "Bất động sản", "Luật sư"]
    },

    9: {
        "title": "Người Nhân Đạo - The Humanitarian",
        "keywords": ["Nhân đạo", "Từ bi", "Hoàn thành", "Lý tưởng", "Phục vụ"],
        "description": """
Bạn có tầm nhìn rộng lớn và mong muốn phục vụ nhân loại. Bạn từ bi, rộng
lượng và có khả năng nhìn vấn đề toàn cầu. Bạn muốn làm cho thế giới tốt
đẹp hơn.
""",
        "strengths": ["Từ bi", "Rộng lượng", "Lý tưởng", "Nghệ thuật"],
        "challenges": ["Không thực tế", "Cảm xúc", "Thiếu ranh giới", "Tự hy sinh"],
        "career": ["Từ thiện", "Giáo dục", "Nghệ thuật", "Tư vấn", "Y tế"]
    },

    11: {
        "title": "Người Truyền Cảm Hứng - The Inspirational Leader",
        "keywords": ["Trực giác", "Truyền cảm hứng", "Tâm linh", "Lý tưởng", "Sáng tạo"],
        "description": """
Số Chủ 11 - Bạn có trực giác mạnh mẽ và khả năng truyền cảm hứng cho người
khác. Bạn là người mơ mộng nhưng cũng có sứ mệnh cao cả. Bạn nhạy cảm và
có khả năng tâm linh đặc biệt.
""",
        "strengths": ["Trực giác cao", "Truyền cảm hứng", "Tâm linh", "Sáng tạo"],
        "challenges": ["Quá nhạy cảm", "Lo âu", "Căng thẳng", "Lý tưởng hóa"],
        "career": ["Giáo viên tâm linh", "Nghệ sĩ", "Nhà tư vấn", "Nhà phát minh", "Trị liệu"]
    },

    22: {
        "title": "Người Xây Dựng Vĩ Đại - The Master Builder",
        "keywords": ["Xây dựng lớn", "Thực tế", "Tầm nhìn", "Lãnh đạo", "Tổ chức"],
        "description": """
Số Chủ 22 - Bạn kết hợp tầm nhìn lớn với khả năng thực thi thực tế. Bạn
có tiềm năng xây dựng những điều vĩ đại phục vụ nhân loại. Bạn là người
thực thi các giấc mơ lớn.
""",
        "strengths": ["Tầm nhìn lớn", "Thực thi tốt", "Lãnh đạo", "Có tổ chức"],
        "challenges": ["Áp lực cao", "Căng thẳng", "Quá tham vọng", "Mất cân bằng"],
        "career": ["Doanh nhân lớn", "Kiến trúc sư", "Chính trị gia", "Nhà từ thiện", "Kỹ sư"]
    },

    33: {
        "title": "Người Thầy Tối Cao - The Master Teacher",
        "keywords": ["Giáo dục", "Chữa lành", "Yêu thương", "Phục vụ", "Từ bi"],
        "description": """
Số Chủ 33 - Bạn là người thầy tối cao với khả năng chữa lành và nâng cao
nhân loại. Bạn kết hợp trí tuệ với tình yêu thương vô điều kiện. Sứ mệnh
của bạn là phục vụ và nâng cao ý thức tập thể.
""",
        "strengths": ["Từ bi cao", "Chữa lành", "Giáo dục", "Yêu thương"],
        "challenges": ["Tự hy sinh quá mức", "Kiệt sức", "Hoàn hảo chủ nghĩa", "Gánh nặng"],
        "career": ["Giáo viên", "Trị liệu", "Tâm linh", "Nghệ thuật", "Từ thiện"]
    }
}

# ========== EXPRESSION NUMBER (Chỉ Số Biểu Đạt) ==========
EXPRESSION = {
    1: {
        "title": "Biểu Đạt Độc Lập",
        "description": "Bạn biểu đạt bản thân qua sự lãnh đạo và độc lập. Tài năng của bạn nằm ở khả năng tiên phong và sáng tạo.",
        "talents": ["Lãnh đạo", "Sáng kiến", "Độc lập", "Quyết đoán"]
    },
    2: {
        "title": "Biểu Đạt Hợp Tác",
        "description": "Bạn biểu đạt bản thân qua sự hợp tác và hòa giải. Tài năng của bạn là kết nối mọi người.",
        "talents": ["Ngoại giao", "Hợp tác", "Trung gian", "Nhạy cảm"]
    },
    3: {
        "title": "Biểu Đạt Sáng Tạo",
        "description": "Bạn biểu đạt bản thân qua nghệ thuật và giao tiếp. Tài năng của bạn là truyền cảm hứng.",
        "talents": ["Nghệ thuật", "Giao tiếp", "Viết lách", "Giải trí"]
    },
    4: {
        "title": "Biểu Đạt Thực Tế",
        "description": "Bạn biểu đạt bản thân qua sự tổ chức và xây dựng. Tài năng của bạn là tạo ra cấu trúc vững chắc.",
        "talents": ["Tổ chức", "Xây dựng", "Quản lý", "Kỹ thuật"]
    },
    5: {
        "title": "Biểu Đạt Tự Do",
        "description": "Bạn biểu đạt bản thân qua sự tự do và đa dạng. Tài năng của bạn là thích nghi và khám phá.",
        "talents": ["Linh hoạt", "Giao tiếp", "Bán hàng", "Du lịch"]
    },
    6: {
        "title": "Biểu Đạt Chăm Sóc",
        "description": "Bạn biểu đạt bản thân qua việc chăm sóc và phục vụ. Tài năng của bạn là tạo sự hài hòa.",
        "talents": ["Chăm sóc", "Tư vấn", "Nghệ thuật", "Giáo dục"]
    },
    7: {
        "title": "Biểu Đạt Trí Tuệ",
        "description": "Bạn biểu đạt bản thân qua trí tuệ và phân tích. Tài năng của bạn là tìm kiếm chân lý.",
        "talents": ["Phân tích", "Nghiên cứu", "Tâm linh", "Công nghệ"]
    },
    8: {
        "title": "Biểu Đạt Quyền Lực",
        "description": "Bạn biểu đạt bản thân qua thành công và quyền lực. Tài năng của bạn là tổ chức và quản lý.",
        "talents": ["Kinh doanh", "Quản lý", "Tài chính", "Lãnh đạo"]
    },
    9: {
        "title": "Biểu Đạt Nhân Đạo",
        "description": "Bạn biểu đạt bản thân qua phục vụ nhân loại. Tài năng của bạn là từ bi và nghệ thuật.",
        "talents": ["Từ thiện", "Nghệ thuật", "Giảng dạy", "Chữa lành"]
    },
    11: {
        "title": "Biểu Đạt Truyền Cảm Hứng",
        "description": "Bạn biểu đạt bản thân qua trực giác và truyền cảm hứng. Tài năng của bạn là nâng cao người khác.",
        "talents": ["Trực giác", "Truyền cảm hứng", "Tâm linh", "Lãnh đạo tinh thần"]
    },
    22: {
        "title": "Biểu Đạt Xây Dựng Lớn",
        "description": "Bạn biểu đạt bản thân qua xây dựng những điều vĩ đại. Tài năng của bạn là biến tầm nhìn thành hiện thực.",
        "talents": ["Xây dựng lớn", "Tổ chức", "Lãnh đạo", "Tầm nhìn"]
    },
    33: {
        "title": "Biểu Đạt Thầy Giáo",
        "description": "Bạn biểu đạt bản thân qua việc giảng dạy và chữa lành. Tài năng của bạn là yêu thương vô điều kiện.",
        "talents": ["Giảng dạy", "Chữa lành", "Từ bi", "Nghệ thuật"]
    }
}

# ========== SOUL URGE NUMBER (Chỉ Số Linh Hồn) ==========
SOUL_URGE = {
    1: {
        "title": "Khao Khát Độc Lập",
        "description": "Sâu thẳm trong lòng, bạn khao khát tự do và độc lập. Bạn muốn là người dẫn đầu và làm theo cách riêng của mình.",
        "desires": ["Tự chủ", "Lãnh đạo", "Sáng tạo", "Công nhận"]
    },
    2: {
        "title": "Khao Khát Hòa Bình",
        "description": "Bạn khao khát hòa bình, hài hòa và mối quan hệ sâu sắc. Bạn muốn được yêu thương và cảm thấy thuộc về.",
        "desires": ["Hòa bình", "Mối quan hệ", "Hợp tác", "Yêu thương"]
    },
    3: {
        "title": "Khao Khát Sáng Tạo",
        "description": "Bạn khao khát thể hiện bản thân một cách sáng tạo. Bạn muốn mang niềm vui và cảm hứng cho người khác.",
        "desires": ["Tự do sáng tạo", "Vui vẻ", "Biểu đạt", "Công nhận"]
    },
    4: {
        "title": "Khao Khát Ổn Định",
        "description": "Bạn khao khát sự ổn định và an toàn. Bạn muốn xây dựng nền tảng vững chắc cho tương lai.",
        "desires": ["Ổn định", "An toàn", "Trật tự", "Thành tựu"]
    },
    5: {
        "title": "Khao Khát Tự Do",
        "description": "Bạn khao khát tự do tuyệt đối và trải nghiệm mới. Bạn muốn khám phá thế giới và sống cuộc sống đa dạng.",
        "desires": ["Tự do", "Phiêu lưu", "Đa dạng", "Kích thích"]
    },
    6: {
        "title": "Khao Khát Yêu Thương",
        "description": "Bạn khao khát yêu thương và được yêu thương. Bạn muốn chăm sóc người khác và tạo ra môi trường hài hòa.",
        "desires": ["Yêu thương", "Gia đình", "Hài hòa", "Phục vụ"]
    },
    7: {
        "title": "Khao Khát Chân Lý",
        "description": "Bạn khao khát hiểu biết sâu sắc và chân lý. Bạn muốn khám phá bí ẩn của cuộc sống và vũ trụ.",
        "desires": ["Chân lý", "Hiểu biết", "Tâm linh", "Hoàn hảo"]
    },
    8: {
        "title": "Khao Khát Thành Công",
        "description": "Bạn khao khát thành công và sự công nhận. Bạn muốn đạt được quyền lực và thịnh vượng vật chất.",
        "desires": ["Thành công", "Quyền lực", "Công nhận", "Vật chất"]
    },
    9: {
        "title": "Khao Khát Phục Vụ",
        "description": "Bạn khao khát làm cho thế giới tốt đẹp hơn. Bạn muốn phục vụ nhân loại và thể hiện tình yêu thương.",
        "desires": ["Phục vụ", "Từ bi", "Lý tưởng", "Nghệ thuật"]
    },
    11: {
        "title": "Khao Khát Soi Sáng",
        "description": "Bạn khao khát soi sáng và truyền cảm hứng. Bạn muốn nâng cao ý thức tập thể qua trực giác của mình.",
        "desires": ["Soi sáng", "Truyền cảm hứng", "Tâm linh", "Lãnh đạo tinh thần"]
    },
    22: {
        "title": "Khao Khát Xây Dựng Vĩ Đại",
        "description": "Bạn khao khát xây dựng điều gì đó vĩ đại và bền vững. Bạn muốn để lại di sản cho nhân loại.",
        "desires": ["Di sản", "Xây dựng lớn", "Ảnh hưởng", "Thay đổi thế giới"]
    },
    33: {
        "title": "Khao Khát Nâng Cao Nhân Loại",
        "description": "Bạn khao khát nâng cao và chữa lành nhân loại. Bạn muốn yêu thương và phục vụ ở mức độ cao nhất.",
        "desires": ["Yêu thương vô điều kiện", "Chữa lành", "Nâng cao", "Giáo dục"]
    }
}

# ========== PERSONALITY NUMBER (Chỉ Số Nhân Cách) ==========
PERSONALITY = {
    1: {
        "title": "Ấn Tượng Lãnh Đạo",
        "description": "Người khác nhìn thấy bạn như một nhà lãnh đạo tự tin và quyết đoán. Bạn tỏa ra năng lượng mạnh mẽ và độc lập.",
        "first_impression": ["Tự tin", "Quyết đoán", "Độc lập", "Mạnh mẽ"]
    },
    2: {
        "title": "Ấn Tượng Hòa Nhã",
        "description": "Người khác nhìn thấy bạn như một người dễ gần, nhạy cảm và hòa nhã. Bạn tỏa ra năng lượng ấm áp và thân thiện.",
        "first_impression": ["Dễ gần", "Nhạy cảm", "Hòa nhã", "Hợp tác"]
    },
    3: {
        "title": "Ấn Tượng Vui Vẻ",
        "description": "Người khác nhìn thấy bạn như một người vui vẻ, sáng tạo và hấp dẫn. Bạn tỏa ra năng lượng tích cực.",
        "first_impression": ["Vui vẻ", "Sáng tạo", "Hấp dẫn", "Giao tiếp tốt"]
    },
    4: {
        "title": "Ấn Tượng Đáng Tin",
        "description": "Người khác nhìn thấy bạn như một người đáng tin cậy, thực tế và có tổ chức. Bạn tỏa ra năng lượng ổn định.",
        "first_impression": ["Đáng tin", "Thực tế", "Có tổ chức", "Chuyên nghiệp"]
    },
    5: {
        "title": "Ấn Tượng Năng Động",
        "description": "Người khác nhìn thấy bạn như một người năng động, thú vị và hấp dẫn. Bạn tỏa ra năng lượng tự do.",
        "first_impression": ["Năng động", "Thú vị", "Hấp dẫn", "Linh hoạt"]
    },
    6: {
        "title": "Ấn Tượng Ấm Áp",
        "description": "Người khác nhìn thấy bạn như một người ấm áp, chăm sóc và có trách nhiệm. Bạn tỏa ra năng lượng yêu thương.",
        "first_impression": ["Ấm áp", "Chăm sóc", "Có trách nhiệm", "Hài hòa"]
    },
    7: {
        "title": "Ấn Tượng Bí Ẩn",
        "description": "Người khác nhìn thấy bạn như một người bí ẩn, trí tuệ và sâu sắc. Bạn tỏa ra năng lượng tâm linh.",
        "first_impression": ["Bí ẩn", "Trí tuệ", "Sâu sắc", "Tâm linh"]
    },
    8: {
        "title": "Ấn Tượng Quyền Lực",
        "description": "Người khác nhìn thấy bạn như một người quyền lực, thành công và chuyên nghiệp. Bạn tỏa ra năng lượng uy quyền.",
        "first_impression": ["Quyền lực", "Thành công", "Chuyên nghiệp", "Uy quyền"]
    },
    9: {
        "title": "Ấn Tượng Từ Bi",
        "description": "Người khác nhìn thấy bạn như một người từ bi, rộng lượng và nghệ thuật. Bạn tỏa ra năng lượng yêu thương.",
        "first_impression": ["Từ bi", "Rộng lượng", "Nghệ thuật", "Lý tưởng"]
    },
    11: {
        "title": "Ấn Tượng Truyền Cảm Hứng",
        "description": "Người khác nhìn thấy bạn như một người truyền cảm hứng, sáng ngời và tâm linh. Bạn tỏa ra năng lượng cao.",
        "first_impression": ["Truyền cảm hứng", "Sáng ngời", "Tâm linh", "Đặc biệt"]
    },
    22: {
        "title": "Ấn Tượng Vĩ Đại",
        "description": "Người khác nhìn thấy bạn như một người có tầm nhìn lớn và khả năng thực thi. Bạn tỏa ra năng lượng mạnh mẽ.",
        "first_impression": ["Tầm nhìn", "Mạnh mẽ", "Có khả năng", "Ấn tượng"]
    },
    33: {
        "title": "Ấn Tượng Thầy Giáo",
        "description": "Người khác nhìn thấy bạn như một người thầy, người chữa lành và nguồn yêu thương. Bạn tỏa ra năng lượng thánh thiện.",
        "first_impression": ["Thầy giáo", "Chữa lành", "Yêu thương", "Thánh thiện"]
    }
}

# ========== BIRTHDAY NUMBER (Chỉ Số Ngày Sinh) ==========
BIRTHDAY = {
    1: {"talent": "Lãnh đạo và sáng kiến tự nhiên"},
    2: {"talent": "Ngoại giao và hợp tác tự nhiên"},
    3: {"talent": "Sáng tạo và giao tiếp tự nhiên"},
    4: {"talent": "Tổ chức và xây dựng tự nhiên"},
    5: {"talent": "Linh hoạt và thích nghi tự nhiên"},
    6: {"talent": "Chăm sóc và hài hòa tự nhiên"},
    7: {"talent": "Phân tích và trực giác tự nhiên"},
    8: {"talent": "Quản lý và tổ chức tự nhiên"},
    9: {"talent": "Từ bi và nghệ thuật tự nhiên"},
    11: {"talent": "Trực giác và truyền cảm hứng tự nhiên"},
    22: {"talent": "Xây dựng lớn và lãnh đạo tự nhiên"},
    33: {"talent": "Giảng dạy và chữa lành tự nhiên"}
}

# ========== MATURITY NUMBER (Số Trưởng Thành) ==========
MATURITY = {
    1: {
        "title": "Trưởng Thành Qua Độc Lập",
        "description": "Khi trưởng thành, bạn sẽ phát triển sự độc lập và lãnh đạo mạnh mẽ hơn. Bạn học cách tự tin vào bản thân và dẫn dắt người khác.",
        "development": ["Tự tin hơn", "Lãnh đạo tốt hơn", "Độc lập hơn", "Quyết đoán hơn"]
    },
    2: {
        "title": "Trưởng Thành Qua Hợp Tác",
        "description": "Khi trưởng thành, bạn sẽ học được giá trị của hợp tác và quan hệ. Bạn trở nên nhạy cảm và khéo léo hơn trong giao tiếp.",
        "development": ["Hợp tác tốt hơn", "Nhạy cảm hơn", "Ngoại giao hơn", "Kiên nhẫn hơn"]
    },
    3: {
        "title": "Trưởng Thành Qua Sáng Tạo",
        "description": "Khi trưởng thành, bạn sẽ phát triển khả năng sáng tạo và giao tiếp. Bạn học cách thể hiện bản thân một cách tự do và vui vẻ.",
        "development": ["Sáng tạo hơn", "Giao tiếp tốt hơn", "Vui vẻ hơn", "Biểu đạt tốt hơn"]
    },
    4: {
        "title": "Trưởng Thành Qua Kỷ Luật",
        "description": "Khi trưởng thành, bạn sẽ học được giá trị của kỷ luật và tổ chức. Bạn xây dựng nền tảng vững chắc cho cuộc sống.",
        "development": ["Có tổ chức hơn", "Kỷ luật hơn", "Thực tế hơn", "Đáng tin cậy hơn"]
    },
    5: {
        "title": "Trưởng Thành Qua Tự Do",
        "description": "Khi trưởng thành, bạn sẽ tìm kiếm tự do và trải nghiệm mới. Bạn học cách thích nghi và linh hoạt với thay đổi.",
        "development": ["Linh hoạt hơn", "Phiêu lưu hơn", "Thích nghi tốt hơn", "Cởi mở hơn"]
    },
    6: {
        "title": "Trưởng Thành Qua Trách Nhiệm",
        "description": "Khi trưởng thành, bạn sẽ nhận thêm trách nhiệm chăm sóc người khác. Bạn tìm thấy ý nghĩa qua việc phục vụ và yêu thương.",
        "development": ["Có trách nhiệm hơn", "Chăm sóc hơn", "Yêu thương hơn", "Hài hòa hơn"]
    },
    7: {
        "title": "Trưởng Thành Qua Trí Tuệ",
        "description": "Khi trưởng thành, bạn sẽ phát triển trí tuệ và tâm linh sâu sắc hơn. Bạn tìm kiếm chân lý và hiểu biết nội tâm.",
        "development": ["Trí tuệ hơn", "Tâm linh hơn", "Sâu sắc hơn", "Trực giác hơn"]
    },
    8: {
        "title": "Trưởng Thành Qua Thành Công",
        "description": "Khi trưởng thành, bạn sẽ phát triển khả năng đạt thành công vật chất. Bạn học cách quản lý quyền lực và tài nguyên.",
        "development": ["Thành công hơn", "Quyền lực hơn", "Tổ chức tốt hơn", "Hiệu quả hơn"]
    },
    9: {
        "title": "Trưởng Thành Qua Phục Vụ",
        "description": "Khi trưởng thành, bạn sẽ phát triển tầm nhìn nhân đạo. Bạn muốn đóng góp cho xã hội và làm cho thế giới tốt đẹp hơn.",
        "development": ["Từ bi hơn", "Rộng lượng hơn", "Lý tưởng hơn", "Nghệ thuật hơn"]
    },
    11: {
        "title": "Trưởng Thành Qua Soi Sáng",
        "description": "Khi trưởng thành, bạn sẽ phát triển khả năng truyền cảm hứng và soi sáng người khác. Bạn trở thành nguồn năng lượng tinh thần.",
        "development": ["Trực giác cao hơn", "Truyền cảm hứng hơn", "Tâm linh sâu hơn", "Lãnh đạo tinh thần"]
    },
    22: {
        "title": "Trưởng Thành Qua Xây Dựng Lớn",
        "description": "Khi trưởng thành, bạn sẽ có khả năng xây dựng những điều vĩ đại phục vụ nhân loại. Bạn kết hợp tầm nhìn với thực thi.",
        "development": ["Tầm nhìn lớn hơn", "Thực thi tốt hơn", "Ảnh hưởng lớn hơn", "Di sản bền vững"]
    },
    33: {
        "title": "Trưởng Thành Qua Giáo Dục",
        "description": "Khi trưởng thành, bạn sẽ trở thành người thầy và người chữa lành. Bạn phục vụ nhân loại với tình yêu thương vô điều kiện.",
        "development": ["Từ bi cao hơn", "Chữa lành sâu hơn", "Giáo dục tốt hơn", "Yêu thương vô điều kiện"]
    }
}

# ========== BALANCE NUMBER (Số Cân Bằng) ==========
BALANCE = {
    1: {
        "title": "Cân Bằng Qua Hành Động",
        "description": "Khi đối mặt với khó khăn, bạn có xu hướng hành động quyết đoán và tự tin. Bạn tin vào bản thân và không ngại đối đầu.",
        "approach": ["Hành động ngay", "Tự tin quyết đoán", "Dẫn đầu giải pháp", "Không e ngại"]
    },
    2: {
        "title": "Cân Bằng Qua Hòa Giải",
        "description": "Khi đối mặt với khó khăn, bạn tìm cách hợp tác và hòa giải. Bạn lắng nghe và cân nhắc nhiều góc độ trước khi hành động.",
        "approach": ["Hợp tác với người khác", "Lắng nghe nhiều ý kiến", "Hòa giải xung đột", "Kiên nhẫn chờ đợi"]
    },
    3: {
        "title": "Cân Bằng Qua Giao Tiếp",
        "description": "Khi đối mặt với khó khăn, bạn sử dụng khả năng giao tiếp và sáng tạo. Bạn tìm cách giải quyết vấn đề bằng lời nói và tư duy tích cực.",
        "approach": ["Giao tiếp cởi mở", "Sáng tạo giải pháp", "Lạc quan tích cực", "Biểu đạt cảm xúc"]
    },
    4: {
        "title": "Cân Bằng Qua Tổ Chức",
        "description": "Khi đối mặt với khó khăn, bạn phân tích và tổ chức. Bạn tạo kế hoạch chi tiết và làm việc có hệ thống.",
        "approach": ["Lập kế hoạch chi tiết", "Tổ chức có hệ thống", "Phân tích thực tế", "Làm việc chăm chỉ"]
    },
    5: {
        "title": "Cân Bằng Qua Linh Hoạt",
        "description": "Khi đối mặt với khó khăn, bạn thích nghi nhanh và tìm cách mới. Bạn không bị ràng buộc bởi quy tắc cứng nhắc.",
        "approach": ["Thích nghi nhanh", "Tìm cách mới", "Linh hoạt tư duy", "Chấp nhận thay đổi"]
    },
    6: {
        "title": "Cân Bằng Qua Trách Nhiệm",
        "description": "Khi đối mặt với khó khăn, bạn đảm nhận trách nhiệm và chăm sóc người khác. Bạn tìm cách hài hòa và cân bằng.",
        "approach": ["Đảm nhận trách nhiệm", "Chăm sóc người khác", "Tìm sự hài hòa", "Cân bằng mọi thứ"]
    },
    7: {
        "title": "Cân Bằng Qua Suy Ngẫm",
        "description": "Khi đối mặt với khó khăn, bạn cần thời gian một mình để suy ngẫm. Bạn phân tích sâu và tìm kiếm hiểu biết nội tâm.",
        "approach": ["Suy ngẫm một mình", "Phân tích sâu sắc", "Tìm chân lý", "Tin vào trực giác"]
    },
    8: {
        "title": "Cân Bằng Qua Kiểm Soát",
        "description": "Khi đối mặt với khó khăn, bạn nắm quyền kiểm soát và tổ chức. Bạn sử dụng khả năng quản lý và quyền lực của mình.",
        "approach": ["Nắm quyền kiểm soát", "Tổ chức nguồn lực", "Quản lý hiệu quả", "Quyết đoán mạnh mẽ"]
    },
    9: {
        "title": "Cân Bằng Qua Từ Bi",
        "description": "Khi đối mặt với khó khăn, bạn sử dụng tình yêu thương và hiểu biết. Bạn nhìn vấn đề từ góc độ rộng lớn hơn.",
        "approach": ["Thể hiện từ bi", "Tha thứ rộng lượng", "Nhìn xa trông rộng", "Phục vụ người khác"]
    },
    11: {
        "title": "Cân Bằng Qua Trực Giác",
        "description": "Khi đối mặt với khó khăn, bạn tin vào trực giác và cảm hứng cao hơn. Bạn tìm kiếm sự hướng dẫn từ nội tâm.",
        "approach": ["Tin vào trực giác", "Tìm cảm hứng", "Kết nối tâm linh", "Truyền năng lượng tích cực"]
    },
    22: {
        "title": "Cân Bằng Qua Tầm Nhìn",
        "description": "Khi đối mặt với khó khăn, bạn tạo tầm nhìn lớn và thực thi. Bạn biến thử thách thành cơ hội xây dựng.",
        "approach": ["Tạo tầm nhìn lớn", "Thực thi mạnh mẽ", "Xây dựng giải pháp bền vững", "Lãnh đạo thay đổi"]
    },
    33: {
        "title": "Cân Bằng Qua Yêu Thương",
        "description": "Khi đối mặt với khó khăn, bạn sử dụng yêu thương vô điều kiện và trí tuệ. Bạn chữa lành và nâng cao mọi người.",
        "approach": ["Yêu thương vô điều kiện", "Chữa lành và hỗ trợ", "Giảng dạy và hướng dẫn", "Nâng cao ý thức"]
    }
}

# ========== HIDDEN PASSION NUMBER (Đam Mê Ẩn) ==========
HIDDEN_PASSION = {
    1: {
        "title": "Đam Mê Lãnh Đạo",
        "description": "Bạn có đam mê mãnh liệt với việc dẫn đầu và tiên phong. Bạn muốn là người đầu tiên, người khác biệt và độc lập.",
        "passion": ["Lãnh đạo người khác", "Khởi xướng dự án mới", "Độc lập tự chủ", "Sáng tạo ý tưởng"]
    },
    2: {
        "title": "Đam Mê Hợp Tác",
        "description": "Bạn có đam mê với việc kết nối và hợp tác. Bạn thích làm việc với người khác và xây dựng mối quan hệ.",
        "passion": ["Xây dựng mối quan hệ", "Hợp tác làm việc", "Hòa giải xung đột", "Hỗ trợ người khác"]
    },
    3: {
        "title": "Đam Mê Sáng Tạo",
        "description": "Bạn có đam mê với nghệ thuật, sáng tạo và giao tiếp. Bạn thích thể hiện bản thân và truyền cảm hứng.",
        "passion": ["Sáng tạo nghệ thuật", "Giao tiếp ý tưởng", "Biểu diễn giải trí", "Viết lách sáng tác"]
    },
    4: {
        "title": "Đam Mê Xây Dựng",
        "description": "Bạn có đam mê với việc xây dựng và tổ chức. Bạn thích tạo ra cấu trúc vững chắc và hệ thống rõ ràng.",
        "passion": ["Xây dựng hệ thống", "Tổ chức công việc", "Quản lý dự án", "Tạo nền tảng vững chắc"]
    },
    5: {
        "title": "Đam Mê Tự Do",
        "description": "Bạn có đam mê với tự do, phiêu lưu và trải nghiệm mới. Bạn thích khám phá và thay đổi.",
        "passion": ["Du lịch khám phá", "Trải nghiệm mới", "Thay đổi môi trường", "Gặp gỡ người mới"]
    },
    6: {
        "title": "Đam Mê Chăm Sóc",
        "description": "Bạn có đam mê với việc chăm sóc và phục vụ người khác. Bạn thích tạo sự hài hòa và cân bằng.",
        "passion": ["Chăm sóc gia đình", "Phục vụ cộng đồng", "Tạo sự hài hòa", "Làm đẹp môi trường"]
    },
    7: {
        "title": "Đam Mê Tri Thức",
        "description": "Bạn có đam mê với tri thức, nghiên cứu và tìm kiếm chân lý. Bạn thích phân tích và hiểu biết sâu sắc.",
        "passion": ["Nghiên cứu học tập", "Tìm kiếm chân lý", "Phân tích sâu sắc", "Phát triển tâm linh"]
    },
    8: {
        "title": "Đam Mê Thành Công",
        "description": "Bạn có đam mê với thành công, quyền lực và vật chất. Bạn thích quản lý và đạt được mục tiêu lớn.",
        "passion": ["Đạt thành công lớn", "Quản lý tổ chức", "Kinh doanh làm giàu", "Có quyền lực ảnh hưởng"]
    },
    9: {
        "title": "Đam Mê Nhân Đạo",
        "description": "Bạn có đam mê với việc phục vụ nhân loại. Bạn thích giúp đỡ người khác và làm cho thế giới tốt đẹp hơn.",
        "passion": ["Phục vụ nhân loại", "Từ thiện xã hội", "Nghệ thuật sáng tạo", "Giáo dục truyền bá"]
    }
}

# ========== KARMIC LESSON NUMBERS (Bài Học Nghiệp) ==========
KARMIC_LESSON = {
    1: {
        "title": "Bài Học Về Độc Lập",
        "description": "Bạn cần học cách tự tin và độc lập hơn. Đừng quá phụ thuộc vào người khác, hãy tin vào bản thân và quyết định của mình.",
        "lesson": "Phát triển sự tự tin, độc lập và khả năng lãnh đạo. Đừng sợ làm theo cách riêng của bạn."
    },
    2: {
        "title": "Bài Học Về Hợp Tác",
        "description": "Bạn cần học cách hợp tác và nhạy cảm hơn với người khác. Đừng quá độc lập, hãy học cách làm việc nhóm.",
        "lesson": "Phát triển khả năng hợp tác, ngoại giao và nhạy cảm với cảm xúc người khác."
    },
    3: {
        "title": "Bài Học Về Biểu Đạt",
        "description": "Bạn cần học cách thể hiện bản thân một cách sáng tạo. Đừng giữ cảm xúc và ý tưởng trong lòng, hãy chia sẻ với thế giới.",
        "lesson": "Phát triển khả năng giao tiếp, sáng tạo và thể hiện bản thân một cách tự tin."
    },
    4: {
        "title": "Bài Học Về Kỷ Luật",
        "description": "Bạn cần học cách tổ chức và kỷ luật hơn. Đừng quá linh hoạt hoặc thiếu kế hoạch, hãy xây dựng nền tảng vững chắc.",
        "lesson": "Phát triển tính kỷ luật, tổ chức và làm việc chăm chỉ để đạt mục tiêu."
    },
    5: {
        "title": "Bài Học Về Linh Hoạt",
        "description": "Bạn cần học cách linh hoạt và thích nghi với thay đổi. Đừng quá cứng nhắc, hãy cởi mở với trải nghiệm mới.",
        "lesson": "Phát triển khả năng thích nghi, linh hoạt và chấp nhận thay đổi trong cuộc sống."
    },
    6: {
        "title": "Bài Học Về Trách Nhiệm",
        "description": "Bạn cần học cách đảm nhận trách nhiệm và chăm sóc người khác. Đừng quá tập trung vào bản thân, hãy quan tâm đến gia đình và cộng đồng.",
        "lesson": "Phát triển tính trách nhiệm, khả năng chăm sóc và tạo sự hài hòa trong mối quan hệ."
    },
    7: {
        "title": "Bài Học Về Tâm Linh",
        "description": "Bạn cần học cách phát triển trí tuệ và tâm linh. Đừng quá vật chất hoặc nông cạn, hãy tìm kiếm hiểu biết sâu sắc.",
        "lesson": "Phát triển khả năng phân tích, trí tuệ và tìm kiếm chân lý nội tâm."
    },
    8: {
        "title": "Bài Học Về Quyền Lực",
        "description": "Bạn cần học cách quản lý quyền lực và tài nguyên. Đừng sợ thành công hoặc tiền bạc, hãy học cách sử dụng chúng một cách có trách nhiệm.",
        "lesson": "Phát triển khả năng quản lý, tổ chức và đạt thành công vật chất một cách cân bằng."
    },
    9: {
        "title": "Bài Học Về Từ Bi",
        "description": "Bạn cần học cách từ bi và phục vụ người khác. Đừng quá tập trung vào lợi ích cá nhân, hãy nghĩ đến lợi ích chung.",
        "lesson": "Phát triển tính từ bi, rộng lượng và mong muốn phục vụ nhân loại."
    }
}

# ========== SUBCONSCIOUS SELF (Tiềm Thức) ==========
SUBCONSCIOUS_SELF = {
    1: {
        "description": "Bạn thiếu 1 số trong tên. Tự tin của bạn trong tình huống khẩn cấp khá thấp. Hãy phát triển lòng tự tin và khả năng tự quyết.",
        "confidence_level": "Thấp"
    },
    2: {
        "description": "Bạn thiếu 2 số trong tên. Tự tin của bạn trong tình huống khẩn cấp còn hạn chế. Hãy tin vào bản thân hơn.",
        "confidence_level": "Hạn chế"
    },
    3: {
        "description": "Bạn thiếu 3 số trong tên. Tự tin của bạn trong tình huống khẩn cấp ở mức trung bình. Bạn có thể đối phó nhưng cần cải thiện.",
        "confidence_level": "Trung bình"
    },
    4: {
        "description": "Bạn thiếu 4 số trong tên. Tự tin của bạn trong tình huống khẩn cấp khá tốt. Bạn có thể xử lý hầu hết các tình huống.",
        "confidence_level": "Khá tốt"
    },
    5: {
        "description": "Bạn thiếu 5 số trong tên. Tự tin của bạn trong tình huống khẩn cấp tốt. Bạn có nhiều nguồn lực để đối phó.",
        "confidence_level": "Tốt"
    },
    6: {
        "description": "Bạn thiếu 6 số trong tên. Tự tin của bạn trong tình huống khẩn cấp rất tốt. Bạn có khả năng xử lý tốt các thử thách.",
        "confidence_level": "Rất tốt"
    },
    7: {
        "description": "Bạn thiếu 7 số trong tên. Tự tin của bạn trong tình huống khẩn cấp xuất sắc. Bạn có nhiều kỹ năng để đối phó.",
        "confidence_level": "Xuất sắc"
    },
    8: {
        "description": "Bạn thiếu 8 số trong tên. Tự tin của bạn trong tình huống khẩn cấp cực kỳ cao. Bạn gần như không bao giờ hoảng loạn.",
        "confidence_level": "Cực kỳ cao"
    },
    9: {
        "description": "Bạn có đầy đủ 9 số trong tên. Tự tin của bạn trong tình huống khẩn cấp hoàn hảo. Bạn có tất cả các nguồn lực cần thiết.",
        "confidence_level": "Hoàn hảo"
    }
}

# ========== CORNERSTONE & CAPSTONE (Đá Góc & Đá Chóp) ==========
CORNERSTONE = {
    1: {"meaning": "Bạn tiếp cận cơ hội với sự tự tin, quyết đoán và tinh thần lãnh đạo."},
    2: {"meaning": "Bạn tiếp cận cơ hội với sự hợp tác, nhạy cảm và ngoại giao."},
    3: {"meaning": "Bạn tiếp cận cơ hội với sự sáng tạo, lạc quan và giao tiếp."},
    4: {"meaning": "Bạn tiếp cận cơ hội với sự thực tế, kỷ luật và tổ chức."},
    5: {"meaning": "Bạn tiếp cận cơ hội với sự linh hoạt, phiêu lưu và tò mò."},
    6: {"meaning": "Bạn tiếp cận cơ hội với sự trách nhiệm, chăm sóc và cân nhắc."},
    7: {"meaning": "Bạn tiếp cận cơ hội với sự phân tích, suy ngẫm và trí tuệ."},
    8: {"meaning": "Bạn tiếp cận cơ hội với sự tham vọng, quyền lực và tổ chức."},
    9: {"meaning": "Bạn tiếp cận cơ hội với sự từ bi, lý tưởng và tầm nhìn rộng."}
}

CAPSTONE = {
    1: {"meaning": "Bạn hoàn thành công việc với sự quyết đoán và độc lập."},
    2: {"meaning": "Bạn hoàn thành công việc với sự hợp tác và kiên nhẫn."},
    3: {"meaning": "Bạn hoàn thành công việc với sự sáng tạo và nhiệt huyết."},
    4: {"meaning": "Bạn hoàn thành công việc với sự kiên trì và kỹ lưỡng."},
    5: {"meaning": "Bạn hoàn thành công việc với sự linh hoạt và thích nghi."},
    6: {"meaning": "Bạn hoàn thành công việc với sự trách nhiệm và hoàn hảo."},
    7: {"meaning": "Bạn hoàn thành công việc với sự phân tích và chính xác."},
    8: {"meaning": "Bạn hoàn thành công việc với sự hiệu quả và quyền lực."},
    9: {"meaning": "Bạn hoàn thành công việc với sự từ bi và tầm nhìn rộng."}
}

# ========== PINNACLE NUMBERS (4 Đỉnh Cao) ==========
PINNACLE = {
    1: {
        "title": "Đỉnh Cao Số 1 - Lãnh Đạo",
        "description": "Giai đoạn này yêu cầu bạn phát triển sự độc lập, tự tin và khả năng lãnh đạo. Đây là thời điểm để bạn tự khẳng định mình.",
        "opportunities": ["Khởi nghiệp kinh doanh", "Dẫn đầu dự án", "Phát triển bản thân", "Tạo sự khác biệt"],
        "challenges": ["Tránh ích kỷ", "Học cách hợp tác", "Kiềm chế bướng bỉnh", "Cân bằng tham vọng"]
    },
    2: {
        "title": "Đỉnh Cao Số 2 - Hợp Tác",
        "description": "Giai đoạn này yêu cầu bạn phát triển kỹ năng hợp tác và xây dựng mối quan hệ. Đây là thời điểm để làm việc với người khác.",
        "opportunities": ["Xây dựng đối tác", "Phát triển mối quan hệ", "Hòa giải xung đột", "Hỗ trợ người khác"],
        "challenges": ["Tránh quá nhạy cảm", "Học cách quyết đoán", "Không quá phụ thuộc", "Tự tin hơn"]
    },
    3: {
        "title": "Đỉnh Cao Số 3 - Sáng Tạo",
        "description": "Giai đoạn này yêu cầu bạn phát triển sự sáng tạo và giao tiếp. Đây là thời điểm để thể hiện bản thân một cách tự do.",
        "opportunities": ["Sáng tạo nghệ thuật", "Phát triển giao tiếp", "Biểu diễn giải trí", "Truyền cảm hứng"],
        "challenges": ["Tránh hoang phí năng lượng", "Tập trung hơn", "Kỷ luật bản thân", "Sâu sắc hơn"]
    },
    4: {
        "title": "Đỉnh Cao Số 4 - Xây Dựng",
        "description": "Giai đoạn này yêu cầu bạn làm việc chăm chỉ và xây dựng nền tảng vững chắc. Đây là thời điểm để tạo ra sự ổn định.",
        "opportunities": ["Xây dựng sự nghiệp", "Tạo nền tảng tài chính", "Phát triển kỹ năng", "Tổ chức cuộc sống"],
        "challenges": ["Tránh cứng nhắc", "Linh hoạt hơn", "Cân bằng công việc", "Vui vẻ hơn"]
    },
    5: {
        "title": "Đỉnh Cao Số 5 - Tự Do",
        "description": "Giai đoạn này yêu cầu bạn khám phá tự do và trải nghiệm mới. Đây là thời điểm để thay đổi và phiêu lưu.",
        "opportunities": ["Du lịch khám phá", "Thay đổi sự nghiệp", "Học điều mới", "Gặp người mới"],
        "challenges": ["Tránh thiếu cam kết", "Ổn định hơn", "Kiên nhẫn hơn", "Kỷ luật hơn"]
    },
    6: {
        "title": "Đỉnh Cao Số 6 - Trách Nhiệm",
        "description": "Giai đoạn này yêu cầu bạn đảm nhận trách nhiệm với gia đình và cộng đồng. Đây là thời điểm để phục vụ và chăm sóc.",
        "opportunities": ["Chăm sóc gia đình", "Phục vụ cộng đồng", "Tạo sự hài hòa", "Giúp đỡ người khác"],
        "challenges": ["Tránh kiểm soát quá mức", "Không tự hy sinh", "Cân bằng cho - nhận", "Chăm sóc bản thân"]
    },
    7: {
        "title": "Đỉnh Cao Số 7 - Trí Tuệ",
        "description": "Giai đoạn này yêu cầu bạn phát triển trí tuệ và tâm linh. Đây là thời điểm để học hỏi và tìm kiếm chân lý.",
        "opportunities": ["Học tập nghiên cứu", "Phát triển tâm linh", "Tìm kiếm chân lý", "Phân tích sâu sắc"],
        "challenges": ["Tránh cô lập", "Kết nối người khác", "Không bi quan", "Tin tưởng hơn"]
    },
    8: {
        "title": "Đỉnh Cao Số 8 - Thành Công",
        "description": "Giai đoạn này yêu cầu bạn đạt thành công vật chất và quyền lực. Đây là thời điểm để xây dựng sự nghiệp lớn.",
        "opportunities": ["Thành công kinh doanh", "Đạt quyền lực", "Tích lũy tài sản", "Quản lý tổ chức"],
        "challenges": ["Tránh vật chất hóa", "Cân bằng tâm linh", "Không độc đoán", "Quan tâm người khác"]
    },
    9: {
        "title": "Đỉnh Cao Số 9 - Nhân Đạo",
        "description": "Giai đoạn này yêu cầu bạn phục vụ nhân loại và hoàn thành chu kỳ. Đây là thời điểm để cho đi và chia sẻ.",
        "opportunities": ["Phục vụ nhân loại", "Từ thiện xã hội", "Sáng tạo nghệ thuật", "Chia sẻ trí tuệ"],
        "challenges": ["Tránh lý tưởng hóa", "Thực tế hơn", "Đặt ranh giới", "Không tự hy sinh quá"]
    },
    11: {
        "title": "Đỉnh Cao Số 11 - Soi Sáng",
        "description": "Giai đoạn này yêu cầu bạn truyền cảm hứng và soi sáng người khác. Đây là thời điểm để phát triển trực giác cao.",
        "opportunities": ["Truyền cảm hứng", "Lãnh đạo tinh thần", "Phát triển trực giác", "Sáng tạo đột phá"],
        "challenges": ["Tránh quá căng thẳng", "Cân bằng năng lượng", "Không quá lý tưởng", "Chấp nhận thực tế"]
    },
    22: {
        "title": "Đỉnh Cao Số 22 - Xây Dựng Vĩ Đại",
        "description": "Giai đoạn này yêu cầu bạn xây dựng điều gì đó vĩ đại phục vụ nhân loại. Đây là thời điểm để tạo di sản.",
        "opportunities": ["Xây dựng lớn", "Tạo di sản", "Ảnh hưởng lớn", "Phục vụ nhân loại"],
        "challenges": ["Tránh áp lực quá cao", "Cân bằng cuộc sống", "Không quá tham vọng", "Giữ sức khỏe"]
    },
    33: {
        "title": "Đỉnh Cao Số 33 - Thầy Giáo",
        "description": "Giai đoạn này yêu cầu bạn giảng dạy và chữa lành nhân loại. Đây là thời điểm để yêu thương vô điều kiện.",
        "opportunities": ["Giảng dạy người khác", "Chữa lành tâm hồn", "Yêu thương vô điều kiện", "Nâng cao ý thức"],
        "challenges": ["Tránh kiệt sức", "Chăm sóc bản thân", "Không quá hoàn hảo", "Chấp nhận hạn chế"]
    }
}

# ========== CHALLENGE NUMBERS (4 Số Thử Thách) ==========
CHALLENGE = {
    0: {
        "title": "Thử Thách Số 0 - Tự Do Lựa Chọn",
        "description": "Bạn có tự do lựa chọn mọi thử thách. Đây vừa là cơ hội vừa là thách thức vì bạn phải tự tìm hướng đi.",
        "lesson": "Học cách tự quyết định và chịu trách nhiệm với lựa chọn của mình. Đừng sợ thất bại.",
        "advice": "Khám phá nhiều con đường, thử nghiệm và tìm ra đam mê thực sự của bạn."
    },
    1: {
        "title": "Thử Thách Số 1 - Độc Lập",
        "description": "Thử thách của bạn là phát triển sự tự tin và độc lập. Bạn có thể quá phụ thuộc vào người khác hoặc thiếu quyết đoán.",
        "lesson": "Học cách tin vào bản thân, đưa ra quyết định và không sợ đi theo con đường riêng.",
        "advice": "Thực hành việc đưa ra quyết định nhỏ mỗi ngày. Đừng luôn chờ đợi sự chấp thuận từ người khác."
    },
    2: {
        "title": "Thử Thách Số 2 - Nhạy Cảm",
        "description": "Thử thách của bạn là cân bằng sự nhạy cảm. Bạn có thể quá nhạy cảm hoặc thiếu cảm thông với người khác.",
        "lesson": "Học cách lắng nghe, thấu hiểu nhưng không bị ảnh hưởng quá mức bởi cảm xúc người khác.",
        "advice": "Phát triển ranh giới cảm xúc lành mạnh. Học cách nói không khi cần thiết."
    },
    3: {
        "title": "Thử Thách Số 3 - Biểu Đạt",
        "description": "Thử thách của bạn là thể hiện bản thân một cách tự tin. Bạn có thể gặp khó khăn trong giao tiếp hoặc sáng tạo.",
        "lesson": "Học cách diễn đạt suy nghĩ và cảm xúc một cách rõ ràng. Đừng sợ bị phán xét.",
        "advice": "Thực hành viết lách, nói chuyện trước đám đông hoặc sáng tạo nghệ thuật thường xuyên."
    },
    4: {
        "title": "Thử Thách Số 4 - Kỷ Luật",
        "description": "Thử thách của bạn là phát triển kỷ luật và tổ chức. Bạn có thể thiếu cấu trúc hoặc quá cứng nhắc.",
        "lesson": "Học cách cân bằng giữa kỷ luật và linh hoạt. Xây dựng thói quen tốt nhưng vẫn cởi mở.",
        "advice": "Tạo lịch trình rõ ràng nhưng cho phép một số linh hoạt. Làm việc chăm chỉ nhưng cũng biết nghỉ ngơi."
    },
    5: {
        "title": "Thử Thách Số 5 - Thay Đổi",
        "description": "Thử thách của bạn là đối phó với thay đổi. Bạn có thể sợ thay đổi hoặc quá bồn chồn không ổn định.",
        "lesson": "Học cách chấp nhận thay đổi như một phần tự nhiên của cuộc sống. Cân bằng giữa tự do và cam kết.",
        "advice": "Thực hành thích nghi với những thay đổi nhỏ. Tìm sự ổn định trong chính bản thân, không phải hoàn cảnh."
    },
    6: {
        "title": "Thử Thách Số 6 - Trách Nhiệm",
        "description": "Thử thách của bạn là cân bằng trách nhiệm với bản thân và người khác. Bạn có thể tự hy sinh quá mức hoặc quá ích kỷ.",
        "lesson": "Học cách chăm sóc người khác mà không quên bản thân. Đặt ranh giới lành mạnh.",
        "advice": "Thực hành nói không khi cần thiết. Nhớ rằng bạn không thể giúp người khác nếu kiệt sức."
    },
    7: {
        "title": "Thử Thách Số 7 - Tin Tưởng",
        "description": "Thử thách của bạn là học cách tin tưởng. Bạn có thể quá nghi ngờ hoặc cô lập bản thân.",
        "lesson": "Học cách tin tưởng bản thân, người khác và vũ trụ. Cân bằng giữa phân tích và trực giác.",
        "advice": "Thực hành tin tưởng vào trực giác. Kết nối với người khác ngay cả khi cảm thấy khó khăn."
    },
    8: {
        "title": "Thử Thách Số 8 - Quyền Lực",
        "description": "Thử thách của bạn là sử dụng quyền lực một cách có trách nhiệm. Bạn có thể sợ quyền lực hoặc lạm dụng nó.",
        "lesson": "Học cách quản lý quyền lực, tiền bạc và nguồn lực một cách cân bằng và có đạo đức.",
        "advice": "Sử dụng thành công để phục vụ người khác. Nhớ rằng quyền lực đi kèm với trách nhiệm."
    }
}

# ========== BRIDGE NUMBERS (Các Số Cầu Nối) ==========

# Life Path - Expression Bridge (Cầu Nối Đường Đời - Biểu Đạt)
LIFE_PATH_EXPRESSION_BRIDGE = {
    0: {
        "title": "Cầu Nối Số 0 - Hoàn Hảo Hài Hòa",
        "description": "Đường đời và tài năng của bạn hoàn toàn hài hòa. Bạn sinh ra đã sẵn sàng với những công cụ cần thiết để thực hiện sứ mệnh cuộc đời.",
        "harmony_level": "Hoàn hảo",
        "advice": "Bạn rất may mắn! Hãy tận dụng sự hài hòa này để đạt được mục tiêu cuộc đời một cách tự nhiên.",
        "challenge": "Đừng tự mãn. Dù mọi thứ đến dễ dàng, bạn vẫn cần nỗ lực để phát triển."
    },
    1: {
        "title": "Cầu Nối Số 1 - Gần Như Hoàn Hảo",
        "description": "Đường đời và tài năng của bạn rất gần nhau. Bạn chỉ cần điều chỉnh nhỏ để hài hòa hoàn toàn.",
        "harmony_level": "Rất cao",
        "advice": "Tập trung vào những kỹ năng bạn đã có. Chỉ cần thêm chút nỗ lực là bạn sẽ thành công.",
        "challenge": "Chú ý đến những chi tiết nhỏ mà bạn có thể bỏ qua vì quá tự tin."
    },
    2: {
        "title": "Cầu Nối Số 2 - Cân Bằng Tốt",
        "description": "Có một khoảng cách nhỏ giữa đường đời và tài năng. Bạn cần phát triển thêm một số kỹ năng để phù hợp với mục đích cuộc đời.",
        "harmony_level": "Tốt",
        "advice": "Học thêm kỹ năng mới liên quan đến lĩnh vực của bạn. Sự linh hoạt sẽ giúp bạn thành công.",
        "challenge": "Đừng cứng nhắc với những gì bạn đã biết. Hãy cởi mở với việc học hỏi."
    },
    3: {
        "title": "Cầu Nối Số 3 - Cần Nỗ Lực",
        "description": "Có khoảng cách đáng kể giữa đường đời và tài năng. Bạn cần làm việc chăm chỉ để phát triển khả năng phù hợp với sứ mệnh.",
        "harmony_level": "Trung bình",
        "advice": "Đầu tư thời gian vào việc học hỏi và phát triển bản thân. Đừng nản lòng trước khó khăn.",
        "challenge": "Kiên nhẫn với quá trình phát triển. Thành công sẽ đến nhưng cần thời gian."
    },
    4: {
        "title": "Cầu Nối Số 4 - Thách Thức Lớn",
        "description": "Khoảng cách lớn giữa đường đời và tài năng. Bạn cần xây dựng nền tảng vững chắc và làm việc có kỷ luật.",
        "harmony_level": "Thách thức",
        "advice": "Tạo kế hoạch dài hạn và làm việc từng bước. Kỷ luật và kiên trì là chìa khóa.",
        "challenge": "Đừng bỏ cuộc khi gặp khó khăn. Mỗi thử thách là cơ hội để phát triển."
    },
    5: {
        "title": "Cầu Nối Số 5 - Cần Thay Đổi Lớn",
        "description": "Khoảng cách rất lớn giữa đường đời và tài năng. Bạn cần thay đổi đáng kể cách tiếp cận cuộc sống.",
        "harmony_level": "Khó khăn",
        "advice": "Cởi mở với sự thay đổi lớn. Đôi khi bạn cần học hoàn toàn điều mới để thành công.",
        "challenge": "Chấp nhận rằng con đường của bạn có thể rất khác với những gì bạn nghĩ."
    },
    6: {
        "title": "Cầu Nối Số 6 - Trách Nhiệm Nặng Nề",
        "description": "Khoảng cách cực lớn giữa đường đời và tài năng. Bạn cần đảm nhận trách nhiệm lớn trong việc phát triển bản thân.",
        "harmony_level": "Rất khó",
        "advice": "Tìm kiếm sự hướng dẫn và hỗ trợ. Đừng cố làm một mình.",
        "challenge": "Kiên nhẫn và tự tin. Hành trình dài nhưng bạn có khả năng hoàn thành."
    },
    7: {
        "title": "Cầu Nối Số 7 - Cần Trí Tuệ Sâu Sắc",
        "description": "Khoảng cách rất xa giữa đường đời và tài năng. Bạn cần sự chuyển hóa tâm linh và trí tuệ sâu sắc.",
        "harmony_level": "Cực kỳ khó",
        "advice": "Tìm kiếm sự hiểu biết sâu sắc về bản thân. Thiền định và tự vấn sẽ giúp ích.",
        "challenge": "Tin tưởng vào hành trình dù nó có vẻ xa vời. Mọi thứ đều có lý do."
    },
    8: {
        "title": "Cầu Nối Số 8 - Cần Quyền Lực Nội Tại",
        "description": "Khoảng cách tối đa giữa đường đời và tài năng. Bạn cần phát triển sức mạnh nội tại to lớn.",
        "harmony_level": "Cực đoan",
        "advice": "Đây là thử thách lớn nhất nhưng cũng là cơ hội để biến đổi hoàn toàn. Hãy kiên trì.",
        "challenge": "Chấp nhận rằng cuộc đời bạn có thể rất khác biệt và đó là điều đặc biệt."
    }
}

# Soul Urge - Personality Bridge (Cầu Nối Linh Hồn - Nhân Cách)
SOUL_URGE_PERSONALITY_BRIDGE = {
    0: {
        "title": "Cầu Nối Số 0 - Trong Ngoài Như Một",
        "description": "Mong muốn nội tâm và hình ảnh bên ngoài của bạn hoàn toàn nhất quán. Bạn là người chân thành, những gì bạn cảm thấy là những gì bạn thể hiện.",
        "authenticity_level": "Hoàn hảo",
        "advice": "Hãy trân trọng sự chân thực này. Đó là phẩm chất quý giá trong thế giới hiện đại.",
        "challenge": "Đôi khi bạn cần học cách điều chỉnh cách thể hiện cho phù hợp với hoàn cảnh."
    },
    1: {
        "title": "Cầu Nối Số 1 - Rất Chân Thực",
        "description": "Mong muốn nội tâm và hình ảnh bên ngoài gần như giống nhau. Bạn thường thể hiện đúng những gì bạn cảm nhận.",
        "authenticity_level": "Rất cao",
        "advice": "Tiếp tục là chính mình. Người khác đánh giá cao sự trung thực của bạn.",
        "challenge": "Đôi khi cần một chút kín đáo trong một số tình huống chuyên nghiệp."
    },
    2: {
        "title": "Cầu Nối Số 2 - Khá Nhất Quán",
        "description": "Có khoảng cách nhỏ giữa mong muốn nội tâm và hình ảnh bên ngoài. Đôi khi bạn giấu một phần cảm xúc thật.",
        "authenticity_level": "Tốt",
        "advice": "Học cách cân bằng giữa việc chia sẻ và giữ kín. Cả hai đều có lúc cần thiết.",
        "challenge": "Đừng giấu quá nhiều đến mức người thân không hiểu bạn."
    },
    3: {
        "title": "Cầu Nối Số 3 - Hai Mặt Khác Nhau",
        "description": "Có sự khác biệt đáng kể giữa mong muốn nội tâm và hình ảnh bên ngoài. Bạn có xu hướng che giấu cảm xúc thật.",
        "authenticity_level": "Trung bình",
        "advice": "Tìm những người an toàn để chia sẻ cảm xúc thật. Đừng cô lập hoàn toàn.",
        "challenge": "Học cách thể hiện cảm xúc một cách lành mạnh hơn."
    },
    4: {
        "title": "Cầu Nối Số 4 - Mâu Thuẫn Nội Tâm",
        "description": "Khoảng cách lớn giữa mong muốn nội tâm và hình ảnh bên ngoài. Bạn thường cảm thấy mâu thuẫn giữa cái bạn muốn và cái bạn thể hiện.",
        "authenticity_level": "Khó khăn",
        "advice": "Tìm cách thể hiện bản thân chân thực hơn trong môi trường an toàn trước.",
        "challenge": "Đừng sống quá lâu với mặt nạ. Điều đó sẽ làm bạn kiệt sức."
    },
    5: {
        "title": "Cầu Nối Số 5 - Hai Con Người",
        "description": "Khoảng cách rất lớn giữa mong muốn nội tâm và hình ảnh bên ngoài. Bạn như hai con người khác nhau.",
        "authenticity_level": "Rất khó",
        "advice": "Làm việc với chuyên gia tâm lý để hòa giải hai mặt của bản thân.",
        "challenge": "Tìm cách kết nối giữa mong muốn thật và cách thể hiện."
    },
    6: {
        "title": "Cầu Nối Số 6 - Chia Rẽ Nội Tâm",
        "description": "Khoảng cách cực lớn giữa mong muốn nội tâm và hình ảnh bên ngoài. Bạn cảm thấy chia rẽ giữa hai thế giới.",
        "authenticity_level": "Cực kỳ khó",
        "advice": "Cần thời gian và công sức để hòa giải. Tìm kiếm hỗ trợ chuyên nghiệp.",
        "challenge": "Học cách chấp nhận và yêu thương cả hai mặt của bản thân."
    },
    7: {
        "title": "Cầu Nối Số 7 - Bí Ẩn Sâu Thẳm",
        "description": "Khoảng cách rất xa giữa mong muốn nội tâm và hình ảnh bên ngoài. Bạn giấu kín phần lớn bản thân thật.",
        "authenticity_level": "Gần như đối lập",
        "advice": "Tìm ít nhất một người bạn đáng tin cậy để chia sẻ bản thân thật.",
        "challenge": "Đừng sống trong sự cô đơn hoàn toàn. Bạn xứng đáng được hiểu."
    },
    8: {
        "title": "Cầu Nối Số 8 - Đối Lập Hoàn Toàn",
        "description": "Khoảng cách tối đa giữa mong muốn nội tâm và hình ảnh bên ngoài. Bạn thể hiện gần như ngược lại với những gì bạn cảm nhận.",
        "authenticity_level": "Đối lập",
        "advice": "Đây là dấu hiệu của sự bảo vệ sâu sắc. Hãy tìm kiếm trị liệu để chữa lành.",
        "challenge": "Từng bước nhỏ để thể hiện bản thân thật. Bạn không cô đơn."
    }
}

# ========== PERSONAL YEAR NUMBER (Năm Cá Nhân) ==========
PERSONAL_YEAR = {
    1: {
        "title": "Năm Khởi Đầu Mới",
        "theme": "Bắt đầu - Độc lập - Hành động",
        "description": "Năm 1 đánh dấu sự khởi đầu của chu kỳ 9 năm. Đây là thời điểm để bắt đầu những dự án mới, đặt mục tiêu mới và khẳng định bản thân.",
        "opportunities": ["Bắt đầu sự nghiệp mới", "Khởi nghiệp kinh doanh", "Phát triển kỹ năng lãnh đạo", "Tạo thay đổi lớn trong cuộc sống"],
        "challenges": ["Tránh quá ích kỷ", "Đừng hành động vội vàng", "Kiên nhẫn với tiến trình", "Cân bằng giữa độc lập và hợp tác"],
        "advice": "Hãy dũng cảm bước ra khỏi vùng an toàn. Năm này thuộc về bạn - đừng sợ làm theo cách riêng của mình."
    },
    2: {
        "title": "Năm Hợp Tác & Mối Quan Hệ",
        "theme": "Kiên nhẫn - Hợp tác - Cân bằng",
        "description": "Năm 2 là thời gian để xây dựng mối quan hệ, hợp tác và phát triển kỹ năng ngoại giao. Hãy chậm lại và nuôi dưỡng các kết nối.",
        "opportunities": ["Xây dựng đối tác kinh doanh", "Phát triển mối quan hệ", "Học kỹ năng ngoại giao", "Hòa giải xung đột"],
        "challenges": ["Tránh quá nhạy cảm", "Đừng mất bản thân trong quan hệ", "Học cách nói không", "Kiên nhẫn với tiến độ chậm"],
        "advice": "Thành công đến qua hợp tác, không phải cạnh tranh. Hãy lắng nghe nhiều hơn nói."
    },
    3: {
        "title": "Năm Sáng Tạo & Vui Vẻ",
        "theme": "Sáng tạo - Giao tiếp - Vui vẻ",
        "description": "Năm 3 mang năng lượng sáng tạo và vui vẻ. Đây là thời gian để thể hiện bản thân, giao tiếp và tận hưởng cuộc sống.",
        "opportunities": ["Phát triển tài năng nghệ thuật", "Cải thiện kỹ năng giao tiếp", "Mở rộng mạng lưới xã hội", "Tận hưởng sở thích"],
        "challenges": ["Tránh phân tán năng lượng", "Đừng quá nông cạn", "Cân bằng vui chơi và công việc", "Tập trung vào mục tiêu"],
        "advice": "Hãy để tâm hồn sáng tạo của bạn tỏa sáng. Đây là năm để nói ra điều bạn muốn nói."
    },
    4: {
        "title": "Năm Làm Việc Chăm Chỉ",
        "theme": "Kỷ luật - Xây dựng - Tổ chức",
        "description": "Năm 4 yêu cầu sự chăm chỉ, kỷ luật và tổ chức. Đây là thời gian để xây dựng nền tảng vững chắc cho tương lai.",
        "opportunities": ["Xây dựng nền tảng tài chính", "Phát triển kỹ năng chuyên môn", "Tổ chức lại cuộc sống", "Đầu tư dài hạn"],
        "challenges": ["Tránh quá cứng nhắc", "Cân bằng công việc và nghỉ ngơi", "Đừng sợ thay đổi", "Kiên nhẫn với kết quả chậm"],
        "advice": "Thành công đến từ nỗ lực kiên trì. Hãy làm việc chăm chỉ ngay hôm nay để gặt hái ngày mai."
    },
    5: {
        "title": "Năm Thay Đổi & Tự Do",
        "theme": "Thay đổi - Tự do - Phiêu lưu",
        "description": "Năm 5 mang năng lượng thay đổi và tự do. Đây là thời gian để khám phá, du lịch và trải nghiệm điều mới.",
        "opportunities": ["Du lịch khám phá", "Thay đổi sự nghiệp", "Học điều mới", "Mở rộng tầm nhìn"],
        "challenges": ["Tránh thiếu cam kết", "Cân bằng tự do và trách nhiệm", "Đừng bồn chồn quá mức", "Hoàn thành những gì đã bắt đầu"],
        "advice": "Hãy đón nhận thay đổi với tâm thế cởi mở. Năm này là để khám phá những gì có thể."
    },
    6: {
        "title": "Năm Trách Nhiệm & Gia Đình",
        "theme": "Trách nhiệm - Yêu thương - Chăm sóc",
        "description": "Năm 6 tập trung vào gia đình, trách nhiệm và phục vụ người khác. Đây là thời gian để nuôi dưỡng và chăm sóc.",
        "opportunities": ["Củng cố quan hệ gia đình", "Chăm sóc người thân", "Cải thiện nhà cửa", "Phục vụ cộng đồng"],
        "challenges": ["Tránh hy sinh quá mức", "Đặt ranh giới lành mạnh", "Chăm sóc bản thân", "Không kiểm soát quá mức"],
        "advice": "Hãy yêu thương và chăm sóc, nhưng đừng quên bản thân. Bạn không thể đổ đầy cho người khác nếu cốc của bạn rỗng."
    },
    7: {
        "title": "Năm Tâm Linh & Nội Tâm",
        "theme": "Tâm linh - Phân tích - Suy ngẫm",
        "description": "Năm 7 là thời gian để rút lui, suy ngẫm và phát triển tâm linh. Đây là năm của sự hiểu biết sâu sắc.",
        "opportunities": ["Phát triển tâm linh", "Học hỏi chuyên sâu", "Tự vấn nội tâm", "Nghiên cứu và phân tích"],
        "challenges": ["Tránh cô lập hoàn toàn", "Cân bằng tâm linh và vật chất", "Tin tưởng trực giác", "Kết nối với người khác"],
        "advice": "Hãy dành thời gian cho bản thân. Những câu trả lời bạn tìm kiếm nằm bên trong."
    },
    8: {
        "title": "Năm Quyền Lực & Thành Công",
        "theme": "Thành công - Quyền lực - Vật chất",
        "description": "Năm 8 mang năng lượng thành công vật chất và quyền lực. Đây là thời gian để đạt được mục tiêu lớn và gặt hái thành quả.",
        "opportunities": ["Thành công trong sự nghiệp", "Thu nhập tăng cao", "Đạt được quyền lực", "Quản lý tài chính tốt"],
        "challenges": ["Tránh vật chất hóa", "Cân bằng công việc và tâm linh", "Sử dụng quyền lực có đạo đức", "Quan tâm đến người khác"],
        "advice": "Đây là năm gặt hái những gì bạn đã gieo. Hãy sử dụng thành công để phục vụ mục đích cao hơn."
    },
    9: {
        "title": "Năm Hoàn Thành & Tha Thứ",
        "theme": "Hoàn thành - Tha thứ - Buông bỏ",
        "description": "Năm 9 đánh dấu kết thúc chu kỳ 9 năm. Đây là thời gian để hoàn thành, tha thứ và buông bỏ những gì không còn phục vụ bạn.",
        "opportunities": ["Hoàn thành dự án cũ", "Tha thứ và hàn gắn", "Phục vụ nhân loại", "Chuẩn bị cho chu kỳ mới"],
        "challenges": ["Buông bỏ quá khứ", "Tha thứ cho bản thân", "Chấp nhận kết thúc", "Không bắt đầu quá nhiều điều mới"],
        "advice": "Hãy dọn dẹp để tạo không gian cho điều mới. Kết thúc là khởi đầu của sự khởi đầu."
    }
}

# ========== PERSONAL MONTH NUMBER (Tháng Cá Nhân) ==========
PERSONAL_MONTH = {
    1: {"theme": "Khởi đầu mới", "focus": "Bắt đầu dự án mới, hành động quyết đoán, tự tin"},
    2: {"theme": "Hợp tác", "focus": "Xây dựng mối quan hệ, kiên nhẫn, ngoại giao"},
    3: {"theme": "Sáng tạo", "focus": "Thể hiện bản thân, giao tiếp, vui vẻ"},
    4: {"theme": "Làm việc chăm chỉ", "focus": "Tổ chức, kỷ luật, xây dựng nền tảng"},
    5: {"theme": "Thay đổi", "focus": "Linh hoạt, thích nghi, khám phá"},
    6: {"theme": "Trách nhiệm", "focus": "Gia đình, chăm sóc, yêu thương"},
    7: {"theme": "Suy ngẫm", "focus": "Nội tâm, học hỏi, tâm linh"},
    8: {"theme": "Thành công", "focus": "Sự nghiệp, tài chính, quyền lực"},
    9: {"theme": "Hoàn thành", "focus": "Kết thúc, tha thứ, phục vụ"}
}

# ========== RATIONAL THOUGHT NUMBER (Số Tư Duy Lý Trí) ==========
RATIONAL_THOUGHT = {
    1: {
        "title": "Tư Duy Độc Lập",
        "description": "Bạn xử lý thông tin một cách độc lập và quyết đoán. Bạn tin vào khả năng phán đoán của bản thân và thích tự đưa ra quyết định.",
        "thinking_style": "Nhanh chóng, tự tin, độc lập",
        "decision_making": "Dựa vào trực giác và logic cá nhân, không cần nhiều ý kiến bên ngoài"
    },
    2: {
        "title": "Tư Duy Cân Bằng",
        "description": "Bạn xử lý thông tin bằng cách cân nhắc nhiều góc độ. Bạn thích lắng nghe ý kiến người khác trước khi quyết định.",
        "thinking_style": "Cẩn thận, cân nhắc, ngoại giao",
        "decision_making": "Tham khảo nhiều nguồn, cân bằng giữa logic và cảm xúc"
    },
    3: {
        "title": "Tư Duy Sáng Tạo",
        "description": "Bạn xử lý thông tin một cách sáng tạo và tích cực. Bạn thường nhìn vấn đề từ góc độ lạc quan và tìm giải pháp sáng tạo.",
        "thinking_style": "Sáng tạo, lạc quan, linh hoạt",
        "decision_making": "Dựa vào cảm hứng, trực giác và khả năng sáng tạo"
    },
    4: {
        "title": "Tư Duy Thực Tế",
        "description": "Bạn xử lý thông tin một cách logic và có hệ thống. Bạn thích phân tích chi tiết và đưa ra quyết định dựa trên sự thật.",
        "thinking_style": "Logic, có hệ thống, chi tiết",
        "decision_making": "Dựa vào dữ liệu, phân tích kỹ lưỡng, kế hoạch cụ thể"
    },
    5: {
        "title": "Tư Duy Linh Hoạt",
        "description": "Bạn xử lý thông tin nhanh chóng và linh hoạt. Bạn có khả năng thích nghi với thay đổi và nhìn vấn đề từ nhiều góc độ.",
        "thinking_style": "Nhanh nhẹn, đa năng, thích nghi",
        "decision_making": "Dựa vào sự linh hoạt, kinh nghiệm đa dạng, phản ứng nhanh"
    },
    6: {
        "title": "Tư Duy Trách Nhiệm",
        "description": "Bạn xử lý thông tin với sự quan tâm đến tác động lên người khác. Bạn cân nhắc yếu tố con người trong mọi quyết định.",
        "thinking_style": "Có trách nhiệm, quan tâm, cân nhắc",
        "decision_making": "Dựa vào tác động đến người khác, giá trị gia đình, trách nhiệm xã hội"
    },
    7: {
        "title": "Tư Duy Phân Tích",
        "description": "Bạn xử lý thông tin một cách sâu sắc và phân tích. Bạn cần thời gian để suy ngẫm trước khi đưa ra quyết định.",
        "thinking_style": "Sâu sắc, phân tích, trực giác",
        "decision_making": "Dựa vào nghiên cứu sâu, trực giác nội tâm, hiểu biết tâm linh"
    },
    8: {
        "title": "Tư Duy Chiến Lược",
        "description": "Bạn xử lý thông tin với tầm nhìn chiến lược. Bạn giỏi nhìn thấy bức tranh lớn và đưa ra quyết định có ảnh hưởng lớn.",
        "thinking_style": "Chiến lược, hiệu quả, quyền lực",
        "decision_making": "Dựa vào mục tiêu lớn, hiệu quả kinh tế, kết quả cụ thể"
    },
    9: {
        "title": "Tư Duy Nhân Đạo",
        "description": "Bạn xử lý thông tin với tầm nhìn rộng và tâm từ bi. Bạn quan tâm đến lợi ích chung và ảnh hưởng toàn cầu.",
        "thinking_style": "Rộng lượng, từ bi, lý tưởng",
        "decision_making": "Dựa vào lợi ích chung, giá trị nhân văn, tầm nhìn toàn cầu"
    },
    11: {
        "title": "Tư Duy Trực Giác Cao",
        "description": "Bạn xử lý thông tin qua trực giác mạnh mẽ. Bạn có khả năng nhận thức vượt trội và thường biết điều gì đúng mà không cần giải thích.",
        "thinking_style": "Trực giác, sáng ngời, truyền cảm hứng",
        "decision_making": "Dựa vào trực giác cao, cảm nhận tinh thần, hướng dẫn nội tâm"
    },
    22: {
        "title": "Tư Duy Xây Dựng Lớn",
        "description": "Bạn xử lý thông tin với khả năng nhìn thấy tiềm năng vĩ đại. Bạn kết hợp tầm nhìn lớn với khả năng thực thi thực tế.",
        "thinking_style": "Tầm nhìn lớn, thực tế, xây dựng",
        "decision_making": "Dựa vào tầm nhìn vĩ đại, khả năng thực hiện, di sản lâu dài"
    }
}


def get_interpretation(category: str, number: int) -> dict:
    """
    Lấy luận giải cho một chỉ số cụ thể

    Args:
        category: Loại chỉ số (
            'life_path', 'expression', 'soul_urge', 'personality', 'birthday',
            'maturity', 'balance', 'hidden_passion', 'karmic_lesson',
            'subconscious_self', 'cornerstone', 'capstone', 'pinnacle', 'challenge',
            'life_path_expression_bridge', 'soul_urge_personality_bridge',
            'personal_year', 'personal_month', 'rational_thought'
        )
        number: Số cần luận giải (0-9, 11, 22, 33)

    Returns:
        Dictionary chứa luận giải
    """
    categories = {
        'life_path': LIFE_PATH,
        'expression': EXPRESSION,
        'soul_urge': SOUL_URGE,
        'personality': PERSONALITY,
        'birthday': BIRTHDAY,
        'maturity': MATURITY,
        'balance': BALANCE,
        'hidden_passion': HIDDEN_PASSION,
        'karmic_lesson': KARMIC_LESSON,
        'subconscious_self': SUBCONSCIOUS_SELF,
        'cornerstone': CORNERSTONE,
        'capstone': CAPSTONE,
        'pinnacle': PINNACLE,
        'challenge': CHALLENGE,
        'life_path_expression_bridge': LIFE_PATH_EXPRESSION_BRIDGE,
        'soul_urge_personality_bridge': SOUL_URGE_PERSONALITY_BRIDGE,
        'personal_year': PERSONAL_YEAR,
        'personal_month': PERSONAL_MONTH,
        'rational_thought': RATIONAL_THOUGHT
    }

    if category not in categories:
        return {"error": f"Unknown category: {category}"}

    if number not in categories[category]:
        return {"error": f"No interpretation for number {number}"}

    return categories[category][number]
