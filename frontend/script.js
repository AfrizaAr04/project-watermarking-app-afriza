const handleUpload = async () => {
  // Ganti URL ini dengan URL Railway kamu yang asli
  const backendUrl = "https://project-watermarking-app-afriza-production-5183.up.railway.app/process-image";

  const formData = new FormData();
  formData.append('file', selectedFile);
  // ... append data lainnya ...

  try {
    const response = await fetch(backendUrl, {
      method: 'POST',
      body: formData,
    });
    const data = await response.json();
    console.log("Berhasil:", data);
  } catch (error) {
    console.error("Gagal terhubung:", error);
  }
};
