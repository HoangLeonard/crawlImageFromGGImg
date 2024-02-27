var imageLinks = []; // Mảng chứa các đường dẫn ảnh

var hoveredElement = null;

document.addEventListener("mouseover", function(event) {
  hoveredElement = event.target;
});

document.addEventListener("keydown", function(event) {
  if (event.key === "s" || event.key === "S") {
    if (hoveredElement.tagName.toLowerCase() === "img") {
      var imageSrc = hoveredElement.src;

      imageLinks.push(imageSrc); // Thêm đường dẫn ảnh vào mảng
      console.log("Đã thêm đường dẫn ảnh:", imageSrc);
    } else {
      console.log("Phần tử không phải là ảnh.");
    }
  } else if (event.key === "d" || event.key === "D") {
    if (imageLinks.length > 0) {
      // Tạo nội dung tập tin chứa các đường dẫn ảnh
      var fileContent = "";
      for (var i = 0; i < imageLinks.length; i++) {
        fileContent += imageLinks[i] + "\n";
      }

      // Tạo một đối tượng Blob từ nội dung tập tin
      var blob = new Blob([fileContent], { type: "text/plain;charset=utf-8" });

      // Tạo một đường dẫn URL từ Blob
      var url = URL.createObjectURL(blob);

      // Tạo một phần tử a để tải xuống tập tin
      var link = document.createElement("a");
      link.href = url;
      link.download = "image_links.txt"; // Tên tập tin khi tải xuống
      document.body.appendChild(link);
      link.click();

      // Giải phóng đường dẫn URL sau khi đã tải xuống
      setTimeout(function() {
        URL.revokeObjectURL(url);
        document.body.removeChild(link);
      }, 0);
    } else {
      console.log("Không có đường dẫn ảnh nào được thêm.");
    }
  }
});