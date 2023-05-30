from bs4 import BeautifulSoup

def extrair_dados_html(html, tag, atributo=None, valor_atributo=None):
    # Analisa o HTML com BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Procura a tag e os atributos desejados
    if atributo and valor_atributo:
        elementos = soup.find_all(tag, {atributo: valor_atributo})
    else:
        elementos = soup.find_all(tag)

    # Extrai o texto dos elementos encontrados
    dados = [elemento.text for elemento in elementos]

    return dados

# Exemplo de uso
html = '''
<table id="crew-member-table" class="table table-sticky thSortable">
                                                <thead>
                                                    <tr class="thead">
                                                        <th class="text-left th-manager-width" data-bind="click: orderByUserName">Manager</th>
                                                        <th class="text-center th-icon-width th-unsortable">Chat</th>
                                                            <th class="text-left th-rank-width" data-bind="click: orderByBattleForm">Battle points</th>
                                                        <th class="text-center th-icon-width" data-bind="click: orderByNationality">Nationality</th>
                                                        <th class="text-left th-login-width" data-bind="click: orderByLastLogin">Last seen</th>
                                                        <th class="text-center th-icon-width" data-bind="click: orderByStatus">Hierarchy</th>
<!-- ko if: isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <th class="text-center th-icon-width th-unsortable">Kick</th>
<!-- /ko -->                                                    </tr>
                                                </thead>
                                                <tbody>
<!-- ko foreach: getItems -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">tbc111</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1347</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">18:50</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon gold" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) -->                                                                <td></td>
<!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">JNPires</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">1083</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">20:22</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="//osm.cloud/Images/Shared/default_userAvatar.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Jota500</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">496</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">21:10</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/129.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">CERQUEIRA_B3770</span>
                                                            </td>
                                                            <td class="text-center" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center hidden" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">397</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">19:18</span>
                                                            </td>
                                                            <td class="text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon silver" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id --><!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) -->                                                                <td></td>
<!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/138.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Pedro Te1xe1r4</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">368</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">19:08</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Ricardo Quintelas</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">343</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">21:07</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Chupapi04</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">159</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-de" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="DE"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">24 May</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="//osm.cloud/Images/Shared/default_userAvatar.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">div1c3</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">132</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">16:03</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Rodolfogio</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">109</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">21:24</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">guilherme_2009_6</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">85</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">3 May</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="//osm.cloud/Images/Shared/default_userAvatar.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Rodrigo Gonçalves 10</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">75</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">28 May</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">PinOkaS</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">56</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">21:14</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon silver" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">nunotiago24</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">48</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">19:06</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="//osm.cloud/Images/Shared/default_userAvatar.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">mamadu candinga</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">42</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">30 January</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">Tuta1994</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">35</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">20:08</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/113.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">RuiMiguelSilva</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">19</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">20:19</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/110.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">jonycorreia68</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">15</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">20:56</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/16.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">vitorino_986</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">14</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">20:17</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/129.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">bit fut 1209</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">10</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">19:53</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/129.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">GomesSporting</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">9</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">19:57</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/39.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">iTzDaniPT</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">4</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">26 May</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko -->                                                        <tr>
                                                            <td class="clickable" data-bind="click: $root.goToUserProfileDelegate.bind($root)">
                                                                <div class="inline-avatar hidden-xs">
                                                                    <img class="avatar" data-bind="inlineImage: getAvatarUrl()" src="https://assets.onlinesoccermanager.com/Avatars/Users/4.jpg?v=3.180.0">
                                                                </div>
                                                                <span class="semi-bold" data-bind="text: userName">C.D.S.Santos</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="css: {'clickable': !isYourAccount() }">
                                                                <span class="semi-bold center" data-bind="css: {'hidden': isYourAccount() }, click: appViewModel.showPmModal.bind(appViewModel, userName)">
                                                                    <span class="fa fa-comments"></span>
                                                                </span>
                                                            </td>
                                                            <td>
                                                                    <span class="semi-bold" data-bind="text: !battleForm ? '-': battleForm">3</span>
                                                            </td>
                                                            <td class="text-center">
                                                                <span class="flag-icon flag-icon-pt" data-bind="css: 'flag-icon-' + (countryCode ? countryCode.toLowerCase() : ''), attr: { title: countryCode }" title="PT"></span>
                                                            </td>
                                                            <td>
                                                                <span class="semi-bold" data-bind="dateFromUnixTimestamp: lastLoginTimestamp">14:40</span>
                                                            </td>
                                                            <td class="text-center clickable" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, status === CrewMemberStatus.Vp ? ($parent.isCrewOwner(appViewModel.userPartial().id) ? CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote :  CrewMemberPartial.EditMemberInfoView.DemoteMember) : CrewMemberPartial.EditMemberInfoView.PromoteMember), css: {'clickable': $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) &amp;&amp; userId !== appViewModel.userPartial().id &amp;&amp; status !== CrewMemberStatus.President }">
                                                                <span class="member-status-ribbon empty" data-bind="css: { 'gold': status === CrewMemberStatus.President, 'silver': status === CrewMemberStatus.Vp, 'empty': status === CrewMemberStatus.Member }"></span>
                                                            </td>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && !$parent.isCrewOwner($data.userId) && $data.userId !== appViewModel.userPartial().id -->                                                                <td class="clickable kick-user-icon text-center" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.KickMember)">
                                                                    <span class="fa fa-times fa-2"></span>
                                                                </td>
<!-- /ko -->                                                            <!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) && ($parent.isCrewOwner($data.userId) || $data.userId === appViewModel.userPartial().id) --><!-- /ko -->                                                        </tr>
<!-- ko if: $parent.isCrewOwnerOrVp(appViewModel.userPartial().id) -->                                                            <tr>
                                                                <td colspan="7" class="edit-member-info kick-user theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.KickMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to kick this member from your Crew?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.kickMember.bind($root, $data),  buttonState: { isLoading: isKickingMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container  row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.PromoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to promote this member to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-positive-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-positive-btn btn-60" data-bind="click: $root.promoteMember.bind($root, $data),  buttonState: { isLoading: isPromoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.DemoteMember" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want to relegate your Captain to member?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.demoteMember.bind($root, $data),  buttonState: { isLoading: isDemoteMemberLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status promote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnershipOrDemote" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden center">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Do you want to change the hierarchy of your Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-wide btn-compact decline-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.DemoteMember)">
                                                                                                <span>Relegate</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primar btn-wide btn-compact accept-positive-btn" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.TransferOwnership)">
                                                                                                <span>Promote</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td colspan="7" class="edit-member-info edit-user-status demote theme-stepover-1">
                                                                    <div class="slide-container row row-h-xs-24" data-bind="slideVisible: visibleEditMemberInfoView() === CrewMemberPartial.EditMemberInfoView.TransferOwnership" style="display: none;">
                                                                        <div class="col-xs-12 col-h-xs-24">
                                                                            <div class="row row-h-xs-24 overflow-hidden">
                                                                                <div class="col-xs-12 col-h-xs-24 edit-info-buttons">
                                                                                    <div class="pull-right">
                                                                                        <span class="inline-block">
                                                                                            Are you sure you want promote your Captain to Boss and relegate yourself to Captain?
                                                                                        </span>
                                                                                        <div class="inline-block">
                                                                                            <button class="btn-new btn-primary btn-compact decline-negative-btn btn-60" data-bind="click: toggleVisibleEditMemberInfoView.bind($data, CrewMemberPartial.EditMemberInfoView.None)">
                                                                                                <span>No</span>
                                                                                            </button>
                                                                                            <button class="btn-new btn-primary btn-compact accept-negative-btn btn-60" data-bind="click: $root.transferOwnership.bind($root, $data), buttonState: { isLoading: isTransferOwnershipLoading() }">
                                                                                                <span>Yes</span>
                                                                                            </button>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </td>
                                                            </tr>
<!-- /ko --><!-- /ko -->                                                    <!-- ko if: $root.crewPartial().isUserMemberOfCrew(appViewModel.userPartial().id) -->                                                        <tr class="custom-crew-row">
                                                            <td colspan="7">
                                                                <div class="row row-h-xs-24 horizontal-right vertical-center">

                                                                    <div class="col-xs-12 col-h-xs-12 text-right">
<!-- ko if: $root.leaveCrewRequestIsLoading --><!-- /ko -->                                                                        <!-- ko ifnot: $root.leaveCrewRequestIsLoading() || $root.leaveCrewRequestIsCompleted() -->                                                                            <a href="#" data-bind="click: $root.confirmLeaveCrew.bind($root, 'Leave Crew', 'Are you sure you want to leave your Crew?')">Leave Crew</a>
<!-- /ko -->                                                                        <div data-bind="fadeVisible: $root.leaveCrewRequestIsCompleted()" style="display: none;">
                                                                            <span class="fa fa-check-circle"></span>
                                                                            You left your Crew!
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
<!-- ko if: count() <= 1 --><!-- /ko --><!-- /ko -->                                                </tbody>
                                            </table>
'''

tag = 'span'
atributo = 'class'
valor_atributo = 'semi-bold'


def remove(ocor,a):
    while ocor in a:
        a.remove(ocor)
    return a

resultado =remove("\n\n",extrair_dados_html(html, tag, atributo, valor_atributo))
print(resultado)
  