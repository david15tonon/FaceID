# Face Enrollment Guide

## Overview

Face enrollment is the process of registering your face in the FaceID system. This allows the system to recognize you in future verification attempts.

## Enrollment Methods

### Method 1: Camera Capture

#### Steps:
1. Navigate to the "Enroll Face" page
2. Select "Camera Capture" option
3. Allow browser access to your camera
4. Position your face within the frame markers
5. Follow the on-screen instructions
6. Click "Capture Face" when ready
7. Review the captured image
8. Click "Confirm" to complete enrollment

#### Tips for Best Results:
- **Lighting**: Ensure even lighting on your face
- **Position**: Face the camera directly
- **Distance**: Stay 1-2 feet from camera
- **Background**: Use a plain background if possible
- **Expression**: Maintain a neutral expression
- **Glasses**: Remove if possible for first enrollment

### Method 2: Image Upload

#### Steps:
1. Navigate to the "Enroll Face" page
2. Select "Upload Image" option
3. Click "Choose file" or drag and drop
4. Select an image from your device
5. Review the uploaded image
6. Fill in user details if required
7. Click "Enroll Face"

#### Image Requirements:
- **Format**: JPG, JPEG, or PNG
- **Size**: Maximum 10MB
- **Quality**: High resolution preferred
- **Content**: Single face, clearly visible
- **Orientation**: Front-facing

## Multiple Face Enrollment

You can enroll multiple face angles to improve recognition accuracy:

1. Front-facing (required)
2. Left profile (optional)
3. Right profile (optional)
4. With glasses (optional)

## Enrollment Verification

After enrollment, the system will:
1. Detect face in the image
2. Generate a unique face encoding
3. Store encoding securely in database
4. Confirm successful enrollment
5. Display enrollment details

## Re-enrollment

Re-enroll your face if:
- Significant appearance change
- Better quality image available
- Low verification confidence scores
- Previous enrollment was poor quality

To re-enroll:
1. Delete existing face enrollment
2. Follow enrollment steps again
3. Use higher quality image

## Security

- Face encodings are stored securely
- Original images can be optionally deleted
- Encodings cannot be reverse-engineered
- Access requires authentication

## Troubleshooting

### "No Face Detected"
- Ensure face is clearly visible
- Check lighting conditions
- Move closer to camera
- Use front-facing angle

### "Poor Image Quality"
- Use better lighting
- Increase image resolution
- Ensure face is in focus
- Avoid motion blur

### "Multiple Faces Detected"
- Ensure only one face in frame
- Remove other people from background
- Crop image to show only your face

## Next Steps

After successful enrollment:
1. Test with face verification
2. Review enrollment in profile
3. Enroll additional angles if needed
4. Update profile information
