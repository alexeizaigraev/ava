const { Router } = require("express");

const AuthController = require("../../controllers/auth");
const { authenticate, upload, uploadImage } = require("../../middlewares");
const router = Router();

router.post(
  "/register",
  AuthController.register
);

router.get("/verify/:verificationToken", AuthController.verify);

router.post(
  "/verify",
  // validateBody(schemas.userEmailSchema),
  AuthController.resendVerify
);

//router.post("/login", validateBody(schemas.loginSchema), AuthController.login);
router.post("/login", AuthController.login);


router.get("/current", authenticate, AuthController.getCurrent);

router.post("/logout",
  authenticate,
  AuthController.logout);

router.patch(
  "/avatars",
  authenticate,
  upload.single("avatar"),
  AuthController.updateAvatar
);

router.put(
  "/:id",
  AuthController.updateUserData
);

router.patch(
  "/user",
  authenticate,
  //validateBody(schemas.updateSubscriptionSchema),
  AuthController.updateSubscription
);

router.patch(
  "/update",
  authenticate,
  uploadImage.single("avatarURL"),
  AuthController.updateUser
);

module.exports = router;
